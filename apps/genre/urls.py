from django.urls import path, include
from .views import GenreCreate, GenreList, GenreDetail, GenreUpdate, GenreDelete
from rest_framework import routers
from apps.genre.api.viewsets import LinkListViewset

router = routers.DefaultRouter()
router.register('listas', LinkListViewset),


urlpatterns = [
    path('criacao/', GenreCreate.as_view(), name='genre-create'),
    path('lista/', GenreList.as_view(), name='genre-list'),
    path('detalhes/<int:pk>/', GenreDetail.as_view(), name='genre-detail'),
    path('atualizacao/<int:pk>/', GenreUpdate.as_view(), name='genre-update'),
    path('delecao/<int:pk>/', GenreDelete.as_view(), name='genre-delete'),
    path('api/', include(router.urls)),
]