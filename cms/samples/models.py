from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class SamplePage(Page):
    parental_page_types = ['samples.SamplesIndexPage']
    content = RichTextField(verbose_name='Содержание')

    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]

    class Meta:
        verbose_name = 'Образец документа'
        verbose_name_plural = 'Образец документа'


class SamplesIndexPage(Page):
    parental_page_types = ['home.HomePage']
    subpage_types = []
    max_count = 1

    class Meta:
        verbose_name = 'Все образцы документов'