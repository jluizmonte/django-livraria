from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.utils.decorators import method_decorator

from .models import Author
from .forms import AuthorForm


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/create.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('author-list')


class AuthorList(ListView):
    model = Author
    template_name = 'author/list.html'
    paginate_by = 10
    ordering = ['-pk']

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author/detail.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/update.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('author-list')


class AuthorDelete(DeleteView):
    model = Author
    template_name = 'author/delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('author-list')