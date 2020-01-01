from django.urls import path
from .views import AuthorCreate, AuthorList, AuthorDetail, AuthorUpdate, AuthorDelete



urlpatterns = [
    path('criacao/', AuthorCreate.as_view(), name='author-create'),
    path('lista/', AuthorList.as_view(), name='author-list'),
    path('detalhes/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('atualizacao/<int:pk>/', AuthorUpdate.as_view(), name='author-update'),
    path('delecao/<int:pk>/', AuthorDelete.as_view(), name='author-delete'),
]