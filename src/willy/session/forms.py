from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils.translation import ugettext as _

class RegistrationForm(auth.forms.UserCreationForm):
    first_name = forms.CharField(label=_('First name'), required=False)
    last_name = forms.CharField(label=_('Last name'), required=False)
    email = forms.EmailField(label=_('E-mail address'), required=True)
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = auth.models.User
        fields = ('first_name', 'last_name', 'email')
