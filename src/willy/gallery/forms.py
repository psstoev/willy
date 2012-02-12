from django import forms

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
    
class PictureUploadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        queryset = None
        if kwargs.has_key('user'):
            queryset = Category.objects.filter(owner=kwargs.pop('user'))
        elif kwargs.has_key('instance'):
            category = kwargs['instance']
            queryset = Category.objects.filter(owner=category.owner).exclude(name=category.name)
        super(PictureUploadForm, self).__init__(*args, **kwargs)
        if queryset is not None:
            self.fields['category'].queryset = queryset


    class Meta:
        model = Picture
        exclude = ('owner', 'uploaded')
