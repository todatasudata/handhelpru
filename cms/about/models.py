from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel


class AboutPage(Page):
    max_count = 1
    main_text = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('main_text')
    ]

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class ConsultantsIndexPage(Page):
    max_count = 1
    subpage_types = ['about.ConsultantPage', ]
    text = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Главная для консультантов'


class ConsultantPage(Page):
    parental_page_types = ['about.ConsultantsIndexPage']
    text = RichTextField(blank=True, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
    )

    class Meta:
        verbose_name = 'Страница консультанта'
        verbose_name_plural = 'Страницы консультантов'


class FriendsPage(Page):
    max_count = 1
    class Meta:
        verbose_name = 'Наши друзья'