from django import forms
from django.db.models import F

from willy.gallery.models import Category, Picture

class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        queryset = None
        if kwargs.has_key('user'):
            queryset = Category.objects.filter(owner=kwargs.pop('user'))
        elif kwargs.has_key('instance'):
            category = kwargs['instance']
            queryset = Category.objects.filter(owner=category.owner).exclude(name=category.name)
        super(CategoryForm, self).__init__(*args, **kwargs)
        if queryset is not None:
            self.fields['category_parent'].queryset = queryset

    class Meta:
        model = Category
        exclude = ('owner')

class CategoryDeleteForm(forms.Form):
    category_id = forms.IntegerField(widget=forms.HiddenInput)
    selected = forms.BooleanField(widget=forms.HiddenInput)
    
class PictureUploadForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = ('owner', 'uploaded', 'pic')
