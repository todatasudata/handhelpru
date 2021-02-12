import operator
from functools import reduce
from django.db import models
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.compat import distinct
from django_filters.rest_framework import DjangoFilterBackend

from .models import ConsPage
from .serializers import ConsPageSerializer


class CustomSearchFilter(filters.SearchFilter):

    def required_m2m_optimization(self, view):
        return getattr(view, 'use_m2m_optimization', True)

    def chained_queryset_filter(self, queryset, search_terms, orm_lookups):
        for search_term in search_terms:
            queries = [
                models.Q(**{orm_lookup: search_term})
                for orm_lookup in orm_lookups
            ]
            queryset = queryset.filter(reduce(operator.or_, queries))
        return queryset

    def optimized_queryset_filter(self, queryset, search_terms, orm_lookups):
        conditions = []
        for search_term in search_terms:
            queries = [
                models.Q(**{orm_lookup: search_term})
                for orm_lookup in orm_lookups
            ]
            conditions.append(reduce(operator.or_, queries))

        return queryset.filter(reduce(operator.and_, conditions))

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)

        if not search_fields or not search_terms:
            return queryset

        orm_lookups = [
            self.construct_search(str(search_field))
            for search_field in search_fields
        ]

        base = queryset
        if self.required_m2m_optimization(view):
            queryset = self.optimized_queryset_filter(queryset, search_terms, orm_lookups)
        else:
            queryset = self.chained_queryset_filter(queryset, search_terms, orm_lookups)

        if self.must_call_distinct(queryset, search_fields):
            queryset = distinct(queryset, base)
        return queryset


class ConsPageViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend, CustomSearchFilter, )
    use_m2m_optimization = False
    search_fields = ('=tags__name', )
    queryset = ConsPage.objects.all()
    serializer_class = ConsPageSerializer

