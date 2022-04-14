from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Customer, SoldProduct


class CustomerForm(ModelForm):
    class Meta: 
        model = Customer
        fields=('firstname','lastname','emailid','contact','address','pincode','aadhaar')

class SoldProductForm(ModelForm):
    class Meta: 
        model = SoldProduct
        # fields="__all__"
        fields=('productid','sellingprice','solddate','cusid')