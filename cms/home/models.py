from django.db import models


from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.api import APIField

from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
    InlinePanel,
    RichTextField
)


class HomePage(Page):
    max_count = 1
    text = RichTextField(blank=True, verbose_name='Текст')
    text_sign = RichTextField(max_length=250, blank=True, verbose_name='Подпись')
    ads = StreamField([
        ('ad', blocks.RichTextBlock(help_text='Объявление', label='Объявление'))
], blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
        FieldPanel('text', heading='Текст'),
        FieldPanel('text_sign', heading='Подпись')], heading='Описание'),
        StreamFieldPanel('ads', heading='Объявления')
    ]

    api_fields = [
        APIField("text"),
        APIField("text_sign"),
        APIField("ads"),
    ]

    class Meta:
        verbose_name = 'Главная страница'

