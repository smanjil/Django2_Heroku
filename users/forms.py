
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        widgets = {
            'first_name': forms.TextInput({
                'placeholder': 'firstname'
            }),
            'last_name': forms.TextInput({
                'placeholder': 'lastname'
            }),
            'username': forms.TextInput({
                'placeholder': 'username'
            }),
            'email': forms.TextInput({
                'placeholder': 'email'
            }),
            'password': forms.PasswordInput({
                'placeholder': 'password'
            })
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput({
                'placeholder': 'username'
            }),
            'password': forms.PasswordInput({
                'placeholder': 'password'
            })
        }