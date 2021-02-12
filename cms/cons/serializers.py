from rest_framework import serializers
from .models import ConsPage
from base import serializers as b_s


class ConsPageSerializer(serializers.ModelSerializer):
    tags = b_s.TagSerializer()

    class Meta:
        model = ConsPage
        fields = ('number', 'content', 'title', 'slug', 'tags')
