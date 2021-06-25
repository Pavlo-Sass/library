from django import forms
from author.models import Author
from .models import Book

# class AddForm(forms.Form):
#
#     name = forms.CharField(max_length=128)
#     description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
#     count = forms.IntegerField()
#     # authors = forms.ModelChoiceField(queryset=Author.get_all())
#     authors = forms.ModelMultipleChoiceField(queryset=Author.get_all())
#     # cover = models.ImageField(upload_to='photos/covers/%Y/%m/%d/', blank=True)
#     cover = forms.ImageField()

class AddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['name', 'description', 'count', 'authors', 'cover']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        #     'count':forms.IntegerField()
        #     'category': forms.Select(attrs={'class': 'form-control'}),
        # }