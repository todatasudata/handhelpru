from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.api import APIField

from base.blocks import NewsBlock


class NewsPage(Page):
    """
    Страница «Новости сайта»
    """
    parental_page_types = ['home.HomePage']
    subpage_types = []

    content = StreamField([
        ('news_item', NewsBlock())
        ], null=True, blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    api_fields = [
        APIField('content'),
    ]

    class Meta:
        verbose_name = 'Страница новостей'


