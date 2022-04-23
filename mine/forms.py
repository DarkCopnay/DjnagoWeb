from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'inputs',
                "placeholder": "Введите свое имя",
                'id': 'name'
            }),
            'email': forms.TextInput(attrs={
                'class': 'inputs',
                "placeholder": "Введите свое имя",
                'title': "Формат почты [domen@gmail.com]",
                'id': 'email'
            }),
            'number': forms.TextInput(attrs={
                'class': 'inputs',
                "placeholder": "Введите свое имя",
                'id': 'number'
            }),
        }