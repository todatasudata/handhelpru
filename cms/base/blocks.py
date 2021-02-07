from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext


class RichTextBlock(blocks.RichTextBlock):

    def get_api_representation(self, value, context=None):
        return richtext(value.source)

    class Meta:
        icon = 'doc-full'
        label = 'Текст'


class NewsBlock(blocks.StructBlock):
    """
    Одна новость сайта
    """
    date = blocks.DateBlock(required=True, label='Дата')
    text = RichTextBlock(required=True, label='Текст')

    class Meta:
        label = 'Новость сайта'