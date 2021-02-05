from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.api import APIField

from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
    RichTextField
)
from wagtail.images.api.fields import ImageRenditionField


class HomePage(Page):
    """Домашняя страница"""

    max_count = 1
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True
    )
    text = RichTextField(blank=True, verbose_name='Текст')
    text_sign = RichTextField(max_length=250, blank=True, verbose_name='Подпись')
    ads = StreamField([
        ('ad', blocks.RichTextBlock(help_text='Объявление', label='Объявление'))
    ], blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('text', heading='Текст'),
            FieldPanel('text_sign', heading='Подпись')],
            heading='Описание'),
        StreamFieldPanel('ads', heading='Объявления'),
        ImageChooserPanel('image', heading='Иллюстрация')
    ]

    api_fields = [
        APIField("text"),
        APIField("text_sign"),
        APIField("ads"),
        APIField("image", serializer=ImageRenditionField('fill-200x250')),
        APIField("image_small", serializer=ImageRenditionField('fill-50x50', source='image'))
    ]

    class Meta:
        verbose_name = 'Главная страница'
