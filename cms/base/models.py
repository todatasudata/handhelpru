from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.api import APIField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.api.fields import ImageRenditionField
from taggit.models import TaggedItemBase, Tag as TaggitTag


@register_snippet
class Author(index.Indexed, models.Model):
    """Авторы для различного контента"""

    surname = models.CharField(max_length=50, verbose_name='Фамилия', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='Имя', null=True, blank=True)
    middle_name = models.CharField(max_length=50, verbose_name='Отчество', null=True, blank=True)
    alias = models.CharField(max_length=50, verbose_name='Псевдоним', null=True, blank=True)
    profession = models.CharField(max_length=200, verbose_name='Профессия/Звание/...', null=True, blank=True)

    # TODO добавить выбор страницы сайта
    
    handhelp_url = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+', on_delete=models.CASCADE,
    verbose_name='Страница на hand-help')
    outer_url = models.URLField(blank=True, null=True, default='hand-help.ru', verbose_name='Страница на стороннем сайте')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, verbose_name='Изображение'
    )
    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    @property
    def short_name(self):  ## Фамилия И.О.
        return f'{self.surname} {self.name[0]}.{self.middle_name[0]}.'

    @property
    def link(self):
        if self.page_url:
            return self.handhelp_url
        elif self.website_url:
            return self.outer_url
        return '#'

    @property
    def ava(self):  # маленькая аватарка
        return self.image.get_rendition('fill-24x24')

    panels = [
        MultiFieldPanel([
            FieldPanel('surname'),
            FieldPanel('name'),
            FieldPanel('middle_name')
        ], heading='ФИО'),
        FieldPanel('alias'),
        FieldPanel('profession'),
        MultiFieldPanel([
            PageChooserPanel('handhelp_url'),
            FieldPanel('outer_url')
        ], heading='Страница'),
        ImageChooserPanel('image'),
    ]

    api_fields = [
        APIField('alias'),
        APIField('profession'),
        APIField('image', serializer=ImageRenditionField('fill-100x100')), #  TODO размеры по макету
        APIField('image_small', serializer=ImageRenditionField('fill-20x20', source='image'))
    ]

    search_fields = [
        index.SearchField('full_name', partial_match=True)
    ]

    def __str__(self):
        return self.full_name  # TODO исправить с учетом разных контекстов, изменить порядок на ФИ

    class Meta:
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




@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']