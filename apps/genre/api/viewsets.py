from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from apps.genre.models import Genre
from .serializers import LinkSerializer


class ListViewSet(ListModelMixin, viewsets.GenericViewSet):
    pass


class LinkListViewset(ListViewSet):
    queryset = Genre.objects.all()
    serializer_class = LinkSerializer
