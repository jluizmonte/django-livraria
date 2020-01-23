from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View
from .models import ShoppingCart
from apps.book.models import Book


class ShoppingCartView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if ShoppingCart.objects.filter(user=request.user).exists():
                shoppingcart = ShoppingCart.objects.get(user=request.user)
                if Book.objects.filter(pk=kwargs['book']).exists():
                    book = Book.objects.get(pk=kwargs['book'])
                    if not ShoppingCart.objects.filter(user=request.user, book=book).exists():
                        shoppingcart.book.add(book)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                else:
                    raise Http404
            else:
                if Book.objects.filter(pk=kwargs['book']).exists():
                    book = Book.objects.get(pk=kwargs['book'])
                    shoppingcart = ShoppingCart.objects.create(user=request.user)
                    if not ShoppingCart.objects.filter(user=request.user, book=kwargs['book']).exists():
                        shoppingcart.book.add(book)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                else:
                    raise Http404
        else:
            return redirect(reverse('account_login'))


class RemoveShoppingCartView(View):
    def get(self, request, *args, **kwargs):
        if kwargs['book']:
            if request.user.is_authenticated:
                if ShoppingCart.objects.filter(user=request.user).exists():
                    shoppingcart = ShoppingCart.objects.get(user=request.user)
                    book = Book.objects.get(pk=kwargs['book'])
                    if ShoppingCart.objects.filter(user=request.user, book=book).exists():
                        shoppingcart.book.remove(book)
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                    else:
                        raise Http404
                else:
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                return redirect(reverse('account_login'))
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
