from django.urls import path
from .views import UserCreateView, UserListView, UserUpdateView, UserDeleteView, UserDetailView

urlpatterns = [
    path('cadastro/', UserCreateView.as_view(), name="user-create"),
    path('lista/', UserListView.as_view(), name="user-list"),
    path('atualizacao/<int:pk>/', UserUpdateView.as_view(), name="user-update"),
    path('delecao/<int:pk>/', UserDeleteView.as_view(), name="user-delete"),
    path('detalhes/<int:pk>/', UserDetailView.as_view(), name="user-detail"),
]