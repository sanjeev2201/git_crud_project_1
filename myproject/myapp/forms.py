from dataclasses import fields
from django import forms
from .models import VnModel


class Vn2form(forms.ModelForm):
    class Meta:
        model = VnModel
        fields = '__all__'
        error_messages = {
            'vn2id': {'required': 'Enter vn2-id'},
            'name': {'required': 'Enter employee name'},
            'Email': {'required': 'Enter employee email'},
            'Age': {'required': 'Enter Employee age'},
            'DOJ': {'required': 'YYYY-MM-DAY'},
            'DOG': {'required': 'YYYY-MM-DAY'},
            'Dojob': {'required': 'YYYY-MM-DAY'},
        }

        widgets = {
            'vn2id': forms.TextInput(attrs={'placeholder': 'Enter vn2-id', 'class': 'myclass'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter Employee Name'}),
            'Email': forms.TextInput(attrs={'placeholder': 'Enter Employee Email'}),
            'Age': forms.TextInput(attrs={'placeholder': 'Enter Employee Age'}),
            'DOJ': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DAY'}),
            'DOG': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DAY'}),
            'Dojob': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DAY'})
        }