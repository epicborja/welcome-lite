from django import forms
from joboffers.models import JobOffer


class JobForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        exclude = ('uuid', 'author', 'slug', 'publish')
