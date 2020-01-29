from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Genre
from .forms import GenreForm


class GenreCreate(CreateView):
    template_name = 'genre/create.html'
    model = Genre
    form_class = GenreForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('genre-list-admin')


class GenreList(ListView):
    template_name = 'genre/list.html'
    model = Genre
    paginate_by = 10
    ordering = ['-pk']

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class GenreDetail(DetailView):
    template_name = 'genre/detail.html'
    model = Genre

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class GenreUpdate(UpdateView):
    template_name = 'genre/update.html'
    model = Genre
    form_class = GenreForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('genre-list-admin')


class GenreDelete(DeleteView):
    template_name = 'genre/delete.html'
    model = Genre

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('genre-list-admin')