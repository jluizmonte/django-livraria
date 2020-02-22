from rest_framework.serializers import ModelSerializer
from ..models import ShoppingCart, Item
from apps.book.api.serializers import BookSerializer


class ItemSerializer(ModelSerializer):
    book__detail = BookSerializer(many=False, read_only=True)

    class Meta:
        model = Item
        fields = ('book', 'amount', 'book__detail')

    def create(self, validated_data):
        user = self.context['request'].user
        shopping_cart = self.get_shopping_cart(user)
        if ShoppingCart.objects.filter(pk=shopping_cart.pk, item__book=validated_data['book']).exists():
           Item.objects.filter(shoppingcart__user=user, book=validated_data['book']).update(**validated_data)
        else:
            item = Item.objects.create(**validated_data)
            shopping_cart.item.add(item)
            shopping_cart.save()
        return Item.objects.get(shoppingcart__user=user, book=validated_data['book'])

    def get_shopping_cart(self, user):
        if ShoppingCart.objects.filter(user=user).exists():
            shopping_cart = ShoppingCart.objects.get(user=user)
        else:
            shopping_cart = ShoppingCart.objects.create(user=user)
        return shopping_cart


class ShoppingCartSerializer(ModelSerializer):
    item = ItemSerializer(many=True, read_only=False)

    class Meta:
        model = ShoppingCart
        fields = '__all__'