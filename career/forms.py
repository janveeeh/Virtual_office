from django import forms
from .models import Career
from django.core import validators
class CareerRegistration(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['job_title', 'job_type', 'job_role', 'qualification','key_skills','exp','required_language','location','job_description']
        widgets = {
            'job_title': forms.TextInput(attrs={'class':'form-control'}),
            'job_type': forms.TextInput(attrs={'class':'form-control'}),
            'job_role': forms.TextInput(attrs={'class':'form-control'}),
            'qualification': forms.TextInput(attrs={'class':'form-control'}),
            'key_skills': forms.TextInput(attrs={'class':'form-control'}),
            'exp' : forms.TextInput(attrs={'class':'form-control'}),
            'required_language' : forms.TextInput(attrs={'class':'form-control'}),
            'location' : forms.TextInput(attrs={'class':'form-control'}),
            'job_description' : forms.TextInput(attrs={'class':'form-control'}),
  
            #'job_title': forms.TextInput(attrs={'class':'form-control'}),

        }