from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class LawPage(Page):
    parental_page_types = ['legislation.LegislationIndexPage']
    content = RichTextField(verbose_name='Содержание')

    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]

    class Meta:
        verbose_name = 'Законодательный акт'
        verbose_name_plural = 'Законодательные акты'


class LegislationIndexPage(Page):
    parental_page_types = ['home.HomePage']
    subpage_types = []
    max_count = 1
    class Meta:
        verbose_name = 'Страница Законодательства'