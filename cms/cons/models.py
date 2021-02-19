from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import TaggedItemBase

from wagtail.core import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    RichTextField,
    PageChooserPanel,
    MultiFieldPanel,
    InlinePanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.api.fields import ImageRenditionField

from wagtail.search import index
from wagtail.api import APIField


from .blocks import QuestionBlock, AnswerBlock
from base import serializers
from base.models import Author


class PreviousConsOrderable(Orderable):
    page = ParentalKey("cons.ConsPage", related_name='previous_cons')
    previous_consultation = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    panels = [
        PageChooserPanel('previous_consultation')
    ]

    @property
    def prev_cons_url(self):
        return self.previous_consultation.url

    @property
    def prev_cons_number(self):
        return self.previous_consultation.specific.number

    api_fields = [
        APIField('prev_cons_url'),
        APIField('prev_cons_number'),
    ]


class ConsPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ConsPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class FAQPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'FAQPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,  # TODO проверить, что CASCADE подходит
    )

class ConsPage(Page):
    """Страница консультации"""

    subpage_types = []
    parent_page_types = ['cons.ConsIndexPage']

    # TODO добавить значение по умолчанию
    number = models.PositiveIntegerField(verbose_name='Номер')
    
    tags = ClusterTaggableManager(through=ConsPageTag, blank=True, verbose_name='Теги')

    # TODO добавить значение по умолчанию
    publish_date = models.DateField(null=True, verbose_name='Дата')

    too_old = models.BooleanField(default=False, null=False, verbose_name='Устарела')  # если конса неактаульная, ставим галочку

    # TODO создавать эти поля автоматически
    client_preview = models.CharField(max_length=100, blank=True, verbose_name='Основной клиент')
    question_preview = RichTextField(blank=True, verbose_name='Основной вопрос')

    authors = ParentalManyToManyField(Author, blank=True)

    content = StreamField(
        [
            ('question', QuestionBlock()),
            ('answer', AnswerBlock()),
        ], blank=True, verbose_name='Содержание')

    content_panels = [
        FieldPanel("number"),
        FieldPanel("tags"),
        FieldPanel('publish_date'),
        FieldPanel('client_preview'),
        FieldPanel('question_preview'),
        StreamFieldPanel("content"),
        FieldPanel('too_old'),
        MultiFieldPanel(
            [InlinePanel("previous_cons", label='Консультация')
            ], heading='Предыдущие консультации')
        ]

    @property
    def tag_slugs(self):
        return '\n'.join(self.tags.all().values_list('slug', flat=True))


    search_fields = Page.search_fields + [
        index.SearchField('number'),
        index.FilterField('number'),
        index.SearchField('client_preview'),
        index.SearchField('question_preview'),
        index.SearchField('content'),
        index.SearchField('tag_slugs'),
        index.RelatedFields('tags', [
            index.SearchField('slug'),
            index.FilterField('slug'),
        ]),
        
    ]

    api_fields = [
        APIField('number'),
        APIField('tags', serializer=serializers.TagSerializer()),
        APIField('publish_date', serializer=serializers.DateSerializer()),
        APIField('authors'),
        APIField("client_preview"),
        APIField("question_preview"),
        APIField("content"),
        APIField('previous_cons'),
        APIField('too_old'),
        APIField('authors', serializer=serializers.AuthorSerializer())
    ]

    def clean(self):
        super().clean()
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

        # создаем для авторов консультации отдельные записи в бд
        for block in self.content:
            if block.block_type == 'answer':
                for sub_block in block.value:
                    if sub_block.block_type == 'author':
                        a = Author.objects.get(id=sub_block.value.id)
                        self.authors.add(a)

    def save(self, *args, **kwargs):
        # автоматически создаем заголовок и слаг,
        # добавляя к номеру консультации и ее теги
        pass
        # print(self)
        # title = 'Консультация №' + str(self.number) + ': '
        # print(title)
        # for tag in self.tags.names():
        #     title += tag
        #     title += ', '
        # title = title[:-2]
        # self.title = title

        # slug = str(self.number)
        # for tag in self.tags.slugs():
        #     slug += '-'
        #     slug += tag
        # self.slug = slug
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'

ConsPage._meta.get_field('slug').default = 'default-blank-slug'


class ConsIndexPage(Page):
    """Главная страница консультаций"""
    max_count = 1
    subpage_types = ['cons.ConsPage', 'cons.FAQIndexPage', 'cons.AskPage']
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
        APIField("image", serializer=ImageRenditionField("fill-483x365")) 
    ]

    content_panels = Page.content_panels + [
        FieldPanel('note', heading='Примечание для «Задать вопрос»'),
        StreamFieldPanel('ads', heading='Объявления'),
        FieldPanel('last_consults_note', heading='О режиме публикации'),
        ImageChooserPanel('image', heading='Иллюстрация')
    ]

    class Meta:
        verbose_name = 'Страница консультаций'


class FAQIndexPage(Page):
    max_count = 1
    subpage_types = ['FAQPage',]
    # content = RichTextField()
    # content_panels = Page.content_panels + [
    #     FieldPanel('content')
    # ]

    class Meta:
        verbose_name = 'Частые вопросы Главная'


class FAQPage(Page):
    parental_page_types = ['FAQIndexPage',]
    subpage_types = []
    number = models.PositiveIntegerField(verbose_name='Номер')
    tags = ClusterTaggableManager(through=FAQPageTag, blank=True, verbose_name='Теги')
    content = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('number'),
        FieldPanel('tags'),
        FieldPanel('content'),
    ]

    @property 
    def tag_slugs(self):
        return '\n'.join(self.tags.all().values_list('slug', flat=True))

    search_fields = Page.search_fields + [
        index.SearchField('content'),
        index.FilterField('tags'),
        index.SearchField('tag_slugs'),
    ]

    api_fields = [
    APIField('number'),
    APIField('tags', serializer=serializers.TagSerializer()),
    APIField('content')
    ]
    
    def clean(self):
        super().clean()
        slug = str(self.number)
        for tag in self.tags.slugs():
            slug += '-'
            slug += tag
        self.slug = slug


    class Meta:
        verbose_name = 'Частый вопрос'


class AskPage(Page):
    max_count = 1
    parental_page_type = ['ConsIndexPage', ]
    content = RichTextField()
    
    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]

    api_fields = [
        APIField('content'),
    ]

    class Meta:
        verbose_name = 'Задать вопрос'
