from rest_framework.serializers import ModelSerializer
from ..models import ShoppingCart
from apps.book.api.serializers import BookSerializer
from rest_framework import serializers


class ShoppingCartSerializer(ModelSerializer):
    book = BookSerializer(many=True, read_only=False)
    book__price__sum = serializers.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        model = ShoppingCart
        fields = '__all__'