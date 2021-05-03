from django import forms
from .models import Article

class URLForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['url',]