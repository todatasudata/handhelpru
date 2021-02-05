from django.db import models

from taggit.models import TaggedItemBase, Tag as TaggitTag

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField, RichTextField

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.api import APIField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.api.fields import ImageRenditionField

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from base import blocks as base_blocks
from base import serializers


class BlogAuthorsOrderable(Orderable):
    """
    Выбор одного или нескольких авторов статьи
    """

    page = ParentalKey("blog.BlogArticlePage", related_name="blog_authors")
    author = models.ForeignKey(
        "base.Author",
        on_delete=models.CASCADE,
    )

    panels = [
        SnippetChooserPanel("author"),
    ]

    @property
    def author_name(self):
        return self.author.name

    @property
    def author_website(self):
        return self.author.website

    @property
    def author_image(self):
        return self.author.image

    api_fields = [
        APIField('author_name'),
        APIField('author_website')
    ]


class AllBlogsListingPage(Page):
    """
    Главная всех блогов
    """
    max_count = 1
    subpage_types = ['blog.BlogIndexPage']

    class Meta:
        verbose_name = 'Главная всех блогов'


class BlogIndexPage(Page):
    """
    Главная страница определенного блога
    """
    subpage_types = ['blog.BlogArticlePage']
    max_count = 3
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    description = RichTextField(
        null=True,
        blank=True,
        help_text='Описание блога'
    )

    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True
    )

    api_fields = [
        APIField('subtitle'),
        APIField('description'),
        APIField('image', serializer=ImageRenditionField('fill-400x595'))
    ]

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('description'),
        ImageChooserPanel('image')
    ]


class BlogArticlePage(Page):
    """
    Запись в блоге
    """
    template = 'blog/blog_article_page.html'

    subtitle = RichTextField(null=True, blank=True)
    content = StreamField(
        [
            ('full_richtext', base_blocks.RichTextBlock()),
            ('table', TableBlock(label='Таблица')),
        ], null=True, blank=True, help_text='Содержание')
    tags = ClusterTaggableManager(through='blog.BlogPageTag', blank=True)
    publish_date = models.DateField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', heading='Подзаголовок'),
        StreamFieldPanel('content', heading='Содержание'),
        MultiFieldPanel(
            [
                InlinePanel("blog_authors", label="Author", min_num=1, max_num=4)
            ],
            heading="Автор(ы)"
        ),
        MultiFieldPanel(
            [
                FieldPanel("tags")
            ],
            heading="Теги"
        ),
        FieldPanel('publish_date')
    ]

    api_fields = [
        APIField('subtitle'),
        APIField('content'),
        APIField('tags', serializer=serializers.TagSerializer()),
        APIField('blog_authors'),
        APIField('publish_date')
    ]

    class Meta:
        verbose_name = 'Запись в блоге'
        verbose_name_plural = 'Записи в блогах'


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogArticlePage', related_name='article_tags')


@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
