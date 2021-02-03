from wagtail.core import blocks
from wagtail.snippets.blocks import SnippetChooserBlock
from rest_framework import serializers


class AuthorBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        pass


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
                'author_name': value.name,
                'author_website': value.website
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
