from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, RedirectView
from apps.book.models import Book


class Administrative(TemplateView):
    template_name = 'home/admin.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class Main(TemplateView):
    template_name = 'home/user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Book.objects.all().order_by('-id')[:30]
        context['books'] = reversed(queryset)
        return context


class Home(RedirectView):
    permanent = True

    def get(self, request, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return redirect(reverse('administrative'))
        else:
            return redirect(reverse('main'))
