from django.urls import path
from .views import ShoppingCartView


urlpatterns = [
    path('adicionar/<int:book>/', ShoppingCartView.as_view(), name='shopping-cart-add'),
]