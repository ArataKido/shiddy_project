from django import forms
from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone', 'type_project', 'content']
