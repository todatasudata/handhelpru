from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    RichTextField
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.api.fields import ImageRenditionField

from wagtail.search import index
from wagtail.api import APIField


from .blocks import QuestionBlock, AnswerBlock


class ConsPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ConsPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class ConsPage(Page):
    """Страница консультации"""

    subpage_types = []
    parent_page_types = ['cons.ConsIndexPage']
    number = models.IntegerField(verbose_name='Номер')
    tags = ClusterTaggableManager(through=ConsPageTag, blank=True, verbose_name='Теги')
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
        index.SearchField('number'),
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

    def save(self, *args, **kwargs):
        # автоматически создаем заголовок и слаг,
        # добавляя к номеру консультации и ее теги
        title = 'Консультация №' + str(self.number) + ': '
        for tag in self.tags.names():
            title += tag
            title += ', '
        title = title[:-2]
        self.title = title

        slug = str(self.number)
        for tag in self.tags.slugs():
            slug += '-'
            slug += tag
        self.slug = slug

        super(ConsPage, self).save()

    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'


class ConsIndexPage(Page):
    """Главная страница консультаций"""
    max_count = 1
    subpage_types = ['cons.ConsPage',
                     'cons.FAQPage']
    note = RichTextField(blank=True, verbose_name='Примечание')
    ads = StreamField([
        ('ad', blocks.RichTextBlock(help_text='Объявление', label='Объявление'))
    ], blank=True)
    last_consults_note = RichTextField(blank=True, verbose_name='О режиме публикации')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True
    )

    api_fields = [
        APIField("note"),
        APIField("ads"),
        APIField("last_consults_note"),
        APIField("image", serializer=ImageRenditionField("fill-200x250"))
    ]

    content_panels = Page.content_panels + [
        FieldPanel('note', heading='Примечание для «Задать вопрос»'),
        StreamFieldPanel('ads', heading='Объявления'),
        FieldPanel('last_consults_note', heading='О режиме публикации'),
        ImageChooserPanel('image', heading='Иллюстрация')
    ]

    class Meta:
        verbose_name = 'Страница консультаций'


class FAQPage(Page):
    max_count = 1
    suppage_types = []
    content = RichTextField()
    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]

    class Meta:
        verbose_name = 'Частые вопросы'
