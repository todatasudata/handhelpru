from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class PracticeDocPage(Page):
    parental_page_types = ['practice.PracticeDocksIndexPage']
    content = RichTextField(verbose_name='Содержание')

    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]

    class Meta:
        verbose_name = 'Страница судебного документа'
        verbose_name_plural = 'Страницы судебных документов'


class PracticeDocksIndexPage(Page):
    parental_page_types = ['home.HomePage']
    subpage_types = []
    max_count = 1

    class Meta:
        verbose_name = 'Страница всей судебной практики'