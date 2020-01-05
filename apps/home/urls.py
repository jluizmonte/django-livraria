from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import Administrative, Home, Main


urlpatterns = [
    path('administrativo/', login_required(Administrative.as_view()), name='administrative'),
    path('', Main.as_view(), name='main'),
    path('home/', Home.as_view(), name='home'),
]