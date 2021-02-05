from wagtail.core import blocks


class NewsBlock(blocks.StructBlock):
    """
    Одна новость сайта
    """
    date = blocks.DateBlock(required=True, label='Дата')
    text = blocks.RichTextBlock(required=True, label='Текст')

    class Meta:
        label = 'Новость сайта'


class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        icon = 'doc-full'
        label = 'Текст'


