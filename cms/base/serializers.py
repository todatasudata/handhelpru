from rest_framework.fields import Field


class TagSerializer(Field):
    """Сериалайзер тегов"""

    def to_representation(self, value):
        return [
            {
                "name": tag.name,
                "slug": tag.slug
            }
            for tag in value.all()
        ]
