from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import Admin, Home


urlpatterns = [
    path('administrativo/', login_required(Admin.as_view()), name='administrative'),
    path('', Home.as_view(), name='home'),
]