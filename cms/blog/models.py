from django.db import models
from django import forms

from taggit.models import TaggedItemBase, Tag as TaggitTag


from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField, RichTextField

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.contrib.table_block.blocks import TableBlock

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager

from base import blocks


class BlogAuthorsOrderable(Orderable):
    """Для выбора более чем одного автора у статьи"""

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


class AllBlogsListingPage(Page):
    max_count = 1
    subpage_types = ['blog.BlogIndexPage']

    class Meta:
        verbose_name = 'Главная всех блогов'


class BlogIndexPage(Page):
    subpage_types = ['blog.BlogArticlePage']
    max_count = 3
    content = RichTextField(
        null=True,
        blank=True,
        help_text='Описание блога'
    )

    content_panels = Page.content_panels + [
        FieldPanel('content', )
    ]


class BlogArticlePage(Page):
    """Запись в блоге"""
    template = 'blog/blog_article_page.html'
    tags = ClusterTaggableManager(through='blog.BlogPageTag', blank=True)
    publish_date = models.DateField(blank=True, null=True)
    content = StreamField(
        [
        ('full_richtext', blocks.RichtextBlock()),
        ('table', TableBlock()),
        ]
        , null=True, blank=True, help_text='Содержание')

    content_panels = Page.content_panels + [
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
        FieldPanel('publish_date'),
        StreamFieldPanel('content'),

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