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
