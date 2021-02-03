from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.api import APIField


@register_snippet
class Author(index.Indexed, models.Model):
    """Авторы для различного контента"""

    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
            ],
            heading="Name and Image",
        ),
        MultiFieldPanel(
            [
                FieldPanel("website"),
            ],
            heading="Links"
        )
    ]

    api_fields = [
        APIField('name'),
        APIField('website')
    ]

    search_fields = [
        index.SearchField('name', partial_match=True)
    ]

    def __str__(self):
        return self.name

    class Meta:  # noqa
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class SimplePage(Page):
    content = RichTextField()
    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]

    class Meta:
        verbose_name = 'Обычная страница'
        verbose_name_plural = 'Обычные страницы'