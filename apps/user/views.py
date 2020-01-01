from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import UserCreationFormWithEmail, UserUpdateForm, UserCreationFormAdmin


class UserCreateView(CreateView):
    model = User

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse('user-list')
        else:
            return reverse('login')

    def get_form(self, form_class=UserCreationFormWithEmail):
        if self.request.user.is_superuser:
            form_class = UserCreationFormAdmin
            form_class.base_fields['username'].widget.attrs['class'] = 'form-control'
            form_class.base_fields['email'].widget.attrs['class'] = 'form-control'
            form_class.base_fields['password1'].widget.attrs['class'] = 'form-control'
            form_class.base_fields['password2'].widget.attrs['class'] = 'form-control'
            return form_class(**self.get_form_kwargs())
        else:
            return form_class(**self.get_form_kwargs())

    def get_template_names(self):
        if self.request.user.is_superuser:
            return 'user/create-admin.html'
        else:
            return 'user/create.html'


class UserListView(ListView):
    template_name = 'user/list.html'
    model = User
    paginate_by = 10


class UserUpdateView(UpdateView):
    template_name = 'user/update.html'
    form_class = UserUpdateForm
    model = User
    fields = ('username', 'email')

    def get_success_url(self):
        return reverse('user-list')

    def get_form(self, form_class=UserUpdateForm):
        form_class.base_fields['username'].widget.attrs['class'] = 'form-control'
        form_class.base_fields['email'].widget.attrs['class'] = 'form-control'
        return form_class(**self.get_form_kwargs())


class UserDeleteView(DeleteView):
    template_name = 'user/delete.html'
    model = User

    def get_success_url(self):
        return reverse('user-list')


class UserDetailView(UpdateView):
    template_name = 'user/detail.html'
    model = User
    form_class = UserUpdateForm