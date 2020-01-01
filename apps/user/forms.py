from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', validators=[EmailValidator])

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationFormWithEmail, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserCreationFormAdmin(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', validators=[EmailValidator])

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", 'is_superuser', 'is_staff')

    def save(self, commit=True):
        user = super(UserCreationFormAdmin, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "email", 'is_superuser', 'is_staff')
