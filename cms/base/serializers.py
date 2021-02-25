from rest_framework.fields import Field
import datetime


class TagSerializer(Field):
    """
    Сериалайзер тегов
    """
    def to_representation(self, value):
        return [
            {
                "name": tag.name,
                "slug": tag.slug
            }
            for tag in value.all()
        ]


class DateSerializer(Field):
    """
    Сериалайзер даты
    """
    def to_representation(self, value):
        date_str = value.strftime('%d.%m.%Y')
        return date_str


class AuthorSerializer(Field):
    """
    Сериалайзер авторов
    """
    def to_representation(self, value):
        return [
            {
                'full_name': author.full_name,
                'short_name': author.short_name,
                'alias': author.alias,
                'link': author.link,
                'profession': author.profession,
                'ava': {
                    'url': author.ava.url,
                    'width': author.ava.width,
                    'height': author.ava.height,
                    'alt': author.ava.alt,
                }
                
            } for author in value.all()
        ]