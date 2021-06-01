from django import forms
from .Article import Article

class URLForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['url',]
    
    def getURL(self):
        return self.data['url']