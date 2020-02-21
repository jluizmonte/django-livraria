from rest_framework.serializers import ModelSerializer
from ..models import ShoppingCart, Item, User
from apps.book.api.serializers import BookSerializer
from rest_framework import serializers


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ShoppingCartSerializer(ModelSerializer):
    item = ItemSerializer(many=False, read_only=False)
    item__book__price__sum = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=False)

    class Meta:
        model = ShoppingCart
        fields = '__all__'

    def create(self, validated_data):
        item = validated_data['item']
        object_item = Item.objects.create(**item)
        del validated_data['item']
        shopping_cart = ShoppingCart.objects.create(**validated_data)
        shopping_cart.item = object_item
        shopping_cart.save()
        return shopping_cart
