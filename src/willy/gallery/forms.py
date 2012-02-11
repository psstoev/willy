from django import forms
from django.db.models import F

from willy.gallery.models import Category, Picture

class CategoryForm(forms.ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        if hasattr(self.instance, 'owner'):
            self.fields['category_parent'].queryset=Category.objects.filter(owner=self.instance.owner).exclude(name=self.instance.name)
        elif user:
            self.fields['category_parent'].queryset=Category.objects.filter(owner=user)

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
