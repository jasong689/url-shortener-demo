from django import forms

class BasicUrlForm(forms.Form):
    url = forms.CharField(max_length=2048, label="url")