from django import forms
from .Keyword import Keywords

class SearchForm(forms.ModelForm):
    class Meta:
        model = Keywords
        fields = ['topic',]

    def getKeyWord(self):
        return self.data['topic']