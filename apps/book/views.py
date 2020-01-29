from django.db.models import Q
from django.http import Http404
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.utils.decorators import method_decorator
from .models import Book
from .forms import BookForm


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/create.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('book-list')


class BookList(ListView):
    model = Book
    template_name = 'book/list.html'
    paginate_by = 10
    ordering = ['-pk']

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BookListSlug(ListView):
    model = Book
    template_name = 'book/list-user.html'
    paginate_by = 10

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        instance = Book.objects.filter(genre__link=slug)
        if len(instance) == 0:
            raise Http404("Não encontrado!")
        return instance


class BookDetail(DetailView):
    model = Book
    template_name = 'book/detail.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BookDetailOut(DetailView):
    model = Book
    template_name = 'book/detail-user.html'


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/update.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('book-list')


class BookDelete(DeleteView):
    model = Book
    template_name = 'book/delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('book-list')


class BookSearchList(ListView):
    model = Book
    template_name = 'book/list-user.html'
    paginate_by = 10

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        instance = Book.objects.filter(Q(name__contains=self.request.GET.get('parametro')) | Q(author__name__contains=self.request.GET.get('parametro')) | Q(genre__description__contains=self.request.GET.get('parametro')))
        if len(instance) == 0:
            raise Http404("Não encontrado!")
        return instance