from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Login..."
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': "Password..."
    }))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Login..."
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': "Create password..."
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': "Confirm password..."
    }))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserShippingForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Enter your full name"
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "+7 (___) ___-__-__"
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Enter your address"
    }))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Enter your postal code"
    }))

    class Meta:
        model = User
        fields = ('fullname', 'phone', 'address', 'postal_code')
