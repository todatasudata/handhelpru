from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class ArticlePage(Page):
    parental_page_types = ['library.ArticlesIndexPage']
    content = RichTextField(verbose_name='Содержание')

    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class ArticlesIndexPage(Page):
    parental_page_types = ['home.HomePage']
    subpage_types = []
    max_count = 1

    class Meta:
        verbose_name = 'Библиотека'