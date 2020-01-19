from django.urls import path, re_path
from allauth.account.views import LogoutView, SignupView
from .views import (
    CustomPasswordResetView, CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView, CustomPasswordResetCompleteView
)
from allauth.account.views import email_verification_sent, confirm_email


urlpatterns = [
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('cadastro/', SignupView.as_view(), name='account_signup'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("confirm-email/", email_verification_sent, name="account_email_verification_sent"),
    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", confirm_email, name="account_confirm_email"),
]