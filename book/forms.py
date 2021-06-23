from django import forms
from author.models import Author

class AddForm(forms.Form):

    name = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    count = forms.IntegerField()
    # authors = forms.ModelChoiceField(queryset=Author.get_all())
    authors = forms.ModelMultipleChoiceField(queryset=Author.get_all())