from django import forms

from .models import PublishingCompany


class PublishingCompanyForm(forms.ModelForm):
    class Meta:
        model = PublishingCompany
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PublishingCompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
