from dataclasses import field
from django import forms
from django.forms import ModelForm
from app.models import FormModel

class Homeform(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = '__all__'



    
