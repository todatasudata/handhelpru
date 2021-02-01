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


class ConsultationPage2Tag(TaggedItemBase):
    content_object = ParentalKey(
        'ConsultationPage2',
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
        APIField("blog_authors"),
        APIField("content"),
    ]

    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'


class ConsultationPage2(Page):
    number = models.IntegerField(verbose_name='Номер', blank=True, null=True)
    tags = ClusterTaggableManager(through=ConsultationPageTag, blank=True, verbose_name='Теги')
    publish_date = models.DateField(null=True, verbose_name='Дата')
    client = models.CharField(max_length=100, blank=True, verbose_name='Спрашивает')
    question = RichTextField(verbose_name='Вопрос')
    answer = RichTextField(verbose_name='Ответ')


    content_panels = Page.content_panels + [
        FieldPanel('number'),
        FieldPanel("tags"),
        FieldPanel('publish_date'),
        FieldPanel('client'),
        FieldPanel('question'),
        FieldPanel('answer')
    ]


class ConsultationsIndexPage(Page):
    """Главная страница консультаций"""
    max_count = 1
    subpage_types = ['consultations.ConsultationPage', 'consultations.ConsultationPage2',
                     'consultations.FAQPage']
    content = StreamField(
        [
            ('special_text', blocks.RichTextBlock()),
            ('additional_block', blocks.RichTextBlock())
        ], blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('content')
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
