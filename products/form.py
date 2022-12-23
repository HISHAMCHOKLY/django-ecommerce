from django import forms
from django.forms import ModelForm
from .models import Orders


class StatusForm(ModelForm):
    class meta:
        model=Orders
        fields=('status')
