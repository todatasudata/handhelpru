from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField


class NewsIndexPage(Page):
    max_count = 1
    subpage_types = ['news.NewsPage']

    class Meta:
        verbose_name = 'Страница всех новостей'
        verbose_name_plural = 'Страницы всех новостей'


class NewsPage(Page):
    parental_page_types = ['news.NewsIndexPage']
    subpage_types = []
    date = models.DateField()
    content = RichTextField()

    class Meta:
        verbose_name = 'Страница Новости'
        verbose_name_plural = 'Страницы новостей'