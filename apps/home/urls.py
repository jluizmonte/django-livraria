from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import Admin, Home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('administrativo/', login_required(Admin.as_view()), name='admin'),
    path('', Home.as_view(), name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)