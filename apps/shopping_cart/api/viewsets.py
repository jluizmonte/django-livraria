from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import ShoppingCart
from .serializers import ShoppingCartSerializer


class ShoppingCartViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ShoppingCartSerializer

    def get_queryset(self):
        query = ShoppingCart.objects.filter(user=self.request.user).annotate(Sum('item__book__price'))
        return query

