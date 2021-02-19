from .basic_url import BasicUrlForm
from django import forms

class CustomUrlForm(BasicUrlForm):
    hash = forms.CharField(label="hash", max_length=8)