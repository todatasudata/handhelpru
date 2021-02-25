from wagtail.core import blocks
from wagtail.snippets.blocks import SnippetChooserBlock
from rest_framework import serializers


class ClientBlock(blocks.CharBlock):
    class Meta:
        label = 'Спрашивает'


class QuestionTextBlock(blocks.RichTextBlock):
    class Meta:
        label = 'Текст вопроса'


class QuestionBlock(blocks.StreamBlock):
    client = ClientBlock()
    question_text = QuestionTextBlock()

    class Meta:
        label = 'Спрашивает + Вопрос'


class AuthorBlock(SnippetChooserBlock):
    def __init__(self):
        super().__init__(target_model='base.Author', help_text='Кто отвечает?')

        
    def get_api_representation(self, value, context=None):
        return {
                'full_name': value.full_name,
                'short_name': value.short_name,
                'alias': value.alias,
                'link': value.link,
                'ava': {
                    'url': value.ava.url,
                    'width': value.ava.width,
                    'height': value.ava.height,
                    'alt': value.ava.alt,
                }
        }

    class Meta:
        label = 'Отвечает'


class AnswerTextBlock(blocks.RichTextBlock):
    class Meta:
        label = 'Текст ответа'


class AnswerBlock(blocks.StreamBlock):
    author = AuthorBlock()
    answer_text = AnswerTextBlock()

    class Meta:
        label = 'Отвечает + Ответ'
