from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class GuidelinePage(Page):
    parental_page_types = ['guidelines.GuidelineIndexPage']
    content = RichTextField(verbose_name='Содержание')

    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]

    class Meta:
        verbose_name = 'Памятка'
        verbose_name_plural = 'Памятки'


class GuidelinesIndexPage(Page):
    parental_page_types = ['home.HomePage']
    subpage_types = []
    max_count = 1
    class Meta:
        verbose_name = 'Страница всех памяток'