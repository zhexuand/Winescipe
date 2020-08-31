from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from homebase.models import WinescipeUser

# forms defined here handles user inputs

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = WinescipeUser
        fields = ('username', 'email', 'profile_image')
