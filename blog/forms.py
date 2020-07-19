from django import forms
from django.core.exceptions import ValidationError
from .models import Author, Tag, Category, Post

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    active = forms.BooleanField(required=False)
    created_on = forms.DateTimeField()
    last_logged_in = forms.DateTimeField()

    def clean_name(self):
        name = self.cleaned_data['name']
        name_l = name.lower()
        if name_l == 'admin' or name_l == 'author':
            raise ValidationError("Author name can't be 'admin/author'")
        return name_l

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()

    def save(self):
        new_author = Author.objects.create(
            name = self.cleaned_data['name'],
            email = self.cleaned_data['email'],
            active = self.cleaned_data['active'],
            created_on = self.cleaned_data['created_on'],
            last_logged_in = self.cleaned_data['last_logged_in'],
        )
        return new_author