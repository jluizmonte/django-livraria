from allauth.account.views import LoginView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from apps.shopping_cart.api.viewsets import ShoppingCartViewset


router = routers.DefaultRouter()
router.register(r'carrinho', ShoppingCartViewset, basename='ShoppingCart'),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacao/login/', LoginView.as_view(), name='account_login'),
    path('autenticacao/', include('apps.authentication.urls')),
    path('usuario/', include('apps.user.urls')),
    path('genero/', include('apps.genre.urls')),
    path('autor/', include('apps.author.urls')),
    path('livro/', include('apps.book.urls')),
    path('editora/', include('apps.publishing_company.urls')),
    path('', include('apps.home.urls')),
    path('carrinho/', include('apps.shopping_cart.urls')),
    path('api/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
