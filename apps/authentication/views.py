from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView


class CustomPasswordResetView(PasswordResetView):
    html_email_template_name = 'email/password_reset_email.html'
    from_email = 'livraria@django.com'
    title = 'Alteração de senha'
    template_name = 'account/password_reset_form.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'
