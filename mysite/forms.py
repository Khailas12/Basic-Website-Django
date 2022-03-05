from django import forms
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            'title',
            'author',
            'publish_date',
        ]