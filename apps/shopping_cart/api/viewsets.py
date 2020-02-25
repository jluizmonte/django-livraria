from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import ShoppingCart
from .serializers import ShoppingCartSerializer, ItemSerializer


class CustomItemViewset(generics.CreateAPIView, generics.DestroyAPIView, viewsets.GenericViewSet):
    pass


class CustomShoppingCartViewset(generics.ListAPIView, viewsets.GenericViewSet):
    pass


class ItemViewset(CustomItemViewset):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemSerializer


class ShoppingCartVieset(CustomShoppingCartViewset):
    permission_classes = [IsAuthenticated]
    serializer_class = ShoppingCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)