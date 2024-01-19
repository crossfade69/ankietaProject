from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Poll
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


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

class NoValidationPasswordInput(forms.PasswordInput):
    def value_from_datadict(self, data, files, name):
        return data.get(name)

class PolishUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Nazwa użytkownika'
        self.fields['username'].help_text = (
            'Maks. 150 znaków lub mniej. Tylko litery, cyfry i znaki @/./+/-/_'
        )
        self.fields['password1'].label = 'Hasło'
        self.fields['password1'].help_text = (
            'Hasło musi mieć co najmniej 8 znaków i nie może być zbyt łatwe do odgadnięcia.'
        )
        self.fields['password1'].widget = NoValidationPasswordInput()
        self.fields['password2'].label = 'Potwierdź hasło'
        self.fields['password2'].help_text = 'Wprowadź hasło ponownie dla potwierdzenia.'
        self.fields['password2'].widget = NoValidationPasswordInput()

        def clean_password1(self):
            password1 = self.cleaned_data.get('password1')
            return password1

        def clean_password2(self):
            password2 = self.cleaned_data.get('password2')
            return password2

class PolishEditUsernameForm(UserChangeForm):
    class Meta:
        model = User  # Assuming you have imported the User model
        fields = ['username']

    username = forms.CharField(label='Nazwa użytkownika', max_length=150)

class PolishPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Stare hasło',
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
    new_password1 = forms.CharField(
        label='Nowe hasło',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    new_password2 = forms.CharField(
        label='Potwierdź nowe hasło',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )