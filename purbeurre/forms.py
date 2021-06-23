# Imports
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# User registration form
class SignUpForm(UserCreationForm):
    """Form used to register a user"""
    # email = forms.EmailField(max_length=254, help_text="Veuillez entrer une adresse email valide")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
