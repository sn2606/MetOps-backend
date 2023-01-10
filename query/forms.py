from django import forms

from .models import MetQuery


class MetQueryForm(forms.ModelForm):
    class Meta:
        model = MetQuery
        fields = [
            'latitude',
            'longitude'
        ]
