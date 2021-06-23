import datetime

from django import forms
from authentication.models import CustomUser
from book.models import Book


class AddForm(forms.Form):
    # name = forms.CharField(max_length=20)
    # surname = forms.CharField(max_length=20)
    # patronymic = forms.CharField(max_length=20)

    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # end_at = models.DateTimeField(null=True)
    # plated_end_at = models.DateTimeField()
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    book = forms.ModelChoiceField(queryset=Book.objects.all())
    plated_end_at = forms.DateTimeField(initial=datetime.date.today)
    end_at = forms.DateTimeField(initial=None, required=False)