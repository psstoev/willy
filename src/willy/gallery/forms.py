from django import forms

from willy.gallery.models import Category, Picture

class CategoryForm(forms.ModelForm):
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
