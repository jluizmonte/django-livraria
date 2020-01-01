from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.utils.decorators import method_decorator

from .models import PublishingCompany
from .forms import PublishingCompanyForm


class PublishingCompanyCreate(CreateView):
    model = PublishingCompany
    form_class = PublishingCompanyForm
    template_name = 'publishing_company/create.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('publishing-company-list')


class PublishingCompanyList(ListView):
    model = PublishingCompany
    template_name = 'publishing_company/list.html'
    paginate_by = 10

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PublishingCompanyDetail(DetailView):
    model = PublishingCompany
    template_name = 'publishing_company/detail.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PublishingCompanyUpdate(UpdateView):
    model = PublishingCompany
    form_class = PublishingCompanyForm
    template_name = 'publishing_company/update.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('publishing-company-list')


class PublishingCompanyDelete(DeleteView):
    model = PublishingCompany
    template_name = 'publishing_company/delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/dashboard/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('publishing-company-list')