from rest_framework.serializers import ModelSerializer
from apps.genre.models import Genre


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['link', 'description']