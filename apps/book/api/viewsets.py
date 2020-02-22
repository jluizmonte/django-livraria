from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer
from apps.book.models import Book


class CustomViewset(generics.RetrieveAPIView, viewsets.GenericViewSet):
    pass


class BookViewset(CustomViewset):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(pk=self.kwargs['pk'])