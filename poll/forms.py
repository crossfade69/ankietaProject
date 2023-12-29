from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
#from django.contrib.auth.forms import PasswordChangeForm
from .models import Poll


class EditPollForm(ModelForm):
    new_access_code = forms.CharField(label='New Access Code', max_length=100, required=False)
    new_is_active = forms.BooleanField(required=False)

    class Meta:
        model = Poll
        fields = ['access_code', 'is_active']


class EditUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']



