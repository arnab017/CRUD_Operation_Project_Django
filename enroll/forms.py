from django import forms
from .models import *
from django.core import validators

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter Name',
                'class': 'form-control'}),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter Email',
                'class': 'form-control'}),
            'password': forms.PasswordInput(
                render_value=True,
                attrs={
                'placeholder': 'Enter Password',
                'class': 'form-control'}),
        }