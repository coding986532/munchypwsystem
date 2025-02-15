
from django import forms
from django.forms import ModelForm

from .models import Password, Encryption
class KeyForm(ModelForm):
    Owner = forms.TextInput()
    class Meta:
        model = Encryption
        fields = ['Owner']

class PasswordForm(ModelForm):
    Username = forms.TextInput()
    Password = forms.TextInput()
    TOTP = forms.TextInput()
    Atachment = forms.FileField()
    Date_Created = forms.DateField()
    class Meta:
        model = Password
        fields = ['Username', 'Password', 'TOTP', 'Atachment', 'Date_Created']