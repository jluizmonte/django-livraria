from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class Admin(TemplateView):
    template_name = 'home/admin.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class Home(TemplateView):
    template_name = 'home/user.html'
