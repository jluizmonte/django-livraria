from django.urls import path
from .views import ShoppingCartView, RemoveShoppingCartView


urlpatterns = [
    path('adicionar/<int:book>/', ShoppingCartView.as_view(), name='shopping-cart-add'),
    path('remover/<int:book>/', RemoveShoppingCartView.as_view(), name='shopping-cart-remove'),
]