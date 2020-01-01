from django.urls import path

from .views import BookCreate, BookDelete, BookDetail, BookList, BookUpdate

urlpatterns = [
    path('criacao/', BookCreate.as_view(), name="book-create"),
    path('lista/', BookList.as_view(), name="book-list"),
    path('atualizacao/<int:pk>/', BookUpdate.as_view(), name="book-update"),
    path('delecao/<int:pk>/', BookDelete.as_view(), name="book-delete"),
    path('detalhes/<int:pk>/', BookDetail.as_view(), name="book-detail"),
]