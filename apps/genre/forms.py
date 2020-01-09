from django import forms

from .models import Genre


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GenreForm, self).__init__(*args, **kwargs)

        self.fields['descricao'].widget.attrs['class'] = 'form-control'
        self.fields['link'].widget.attrs['class'] = 'form-control'


