from django import forms

from willy.gallery.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('owner')
