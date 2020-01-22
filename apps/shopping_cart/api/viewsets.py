from django.db.models import Sum, Count
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import ShoppingCart
from .serializers import ShoppingCartSerializer


class Detail(mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class ShoppingCartViewset(Detail):
    permission_classes = [IsAuthenticated]
    serializer_class = ShoppingCartSerializer

    def get_queryset(self):
        query = ShoppingCart.objects.filter(user=self.request.user).annotate(Sum('book__price')).annotate(Count('book'))
        return query
