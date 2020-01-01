from decimal import Decimal

from django import forms
from django.forms import widgets

from .models import Book


class BookForm(forms.ModelForm):

    price = forms.CharField(label='Preço', max_length='6')

    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        self.fields['author'].widget.attrs['class'] = 'form-control'
        self.fields['genre'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['capa'].widget.attrs['class'] = 'form-control'
        self.fields['publishing_company'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control money'

    def clean(self):
        super().clean()
        self.cleaned_data['price'] = Decimal(str(self.cleaned_data['price']).replace('.', '').replace(',', '.'))