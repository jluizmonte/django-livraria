from django.urls import path

from .views import GenreCreate, GenreList, GenreDetail, GenreUpdate, GenreDelete


urlpatterns = [
    path('criacao/', GenreCreate.as_view(), name='genre-create'),
    path('lista/', GenreList.as_view(), name='genre-list'),
    path('detalhes/<int:pk>/', GenreDetail.as_view(), name='genre-detail'),
    path('atualizacao/<int:pk>/', GenreUpdate.as_view(), name='genre-update'),
    path('delecao/<int:pk>/', GenreDelete.as_view(), name='genre-delete'),
]