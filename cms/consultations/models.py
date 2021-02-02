from django.db import models
from django import forms

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import TaggedItemBase

from wagtail.core import blocks

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
    InlinePanel,
    RichTextField
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.api import APIField
from consultations.blocks import QuestionBlock, AnswerBlock


class ConsultationPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ConsultationPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class ConsultationPage(Page):
    """Страница консультации"""

    subpage_types = []
    parent_page_types = ['consultations.ConsultationsIndexPage']
    number = models.IntegerField(verbose_name='Номер')
    tags = ClusterTaggableManager(through=ConsultationPageTag, blank=True, verbose_name='Теги')
    publish_date = models.DateField(null=True, verbose_name='Дата')

    main_client = models.CharField(max_length=100, blank=True, verbose_name='Основной клиент')
    main_question = RichTextField(blank=True, verbose_name='Основной вопрос')

    content = StreamField(
        [
            ('question', QuestionBlock()),
            ('answer', AnswerBlock()),
        ], blank=True, verbose_name='Содержание')

    content_panels = Page.content_panels + [
        FieldPanel("number"),
        FieldPanel("tags"),
        FieldPanel('publish_date'),
        FieldPanel('main_client'),
        FieldPanel('main_question'),
        StreamFieldPanel("content"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('tags'),
        index.SearchField('main_client'),
        index.SearchField('main_question'),
        index.SearchField('content'),
    ]

    api_fields = [
        APIField('number'),
        APIField('tags'),
        APIField('publish_date'),
        APIField("main_client"),
        APIField("main_question"),
        APIField("content"),
    ]

    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'


class ConsultationsIndexPage(Page):
    """Главная страница консультаций"""
    max_count = 1
    subpage_types = ['consultations.ConsultationPage',
                     'consultations.FAQPage']
    note = RichTextField(blank=True, verbose_name='Примечание')
    ads = StreamField([
        ('ad', blocks.RichTextBlock(help_text='Объявление', label='Объявление'))
    ], blank=True)
    last_consults_note = RichTextField(blank=True, verbose_name='О режиме публикации')

    api_fields = [
        APIField("note"),
        APIField("ads"),
        APIField("last_consults_note")
    ]

    content_panels = Page.content_panels + [
        FieldPanel('note', heading='Примечание для «Задать вопрос»'),
        StreamFieldPanel('ads', heading='Объявления'),
        FieldPanel('last_consults_note', heading='О режиме публикации')
    ]

    class Meta:
        verbose_name = 'Страница консультаций'


class FAQPage(Page):
    max_count = 1
    content = RichTextField()
    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]

    class Meta:
        verbose_name = 'Частые вопросы'
