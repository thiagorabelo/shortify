from django import forms

from .models import ShortURI


class ShortURICreateForm(forms.ModelForm):
    class Meta:
        model = ShortURI
        fields = ("full_uri", "description",)
