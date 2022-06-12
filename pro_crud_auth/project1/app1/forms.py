from tkinter import Widget
from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'
        labels = {
            'laptop_id':"LAPTOP ID",
            'name':"NAME",
            'brand':'BRAND',
            'ram':'RAM',
            'rom':'ROM',
            'HDD':'HDD',
            'SSD':'SSD',
            'price':'PRICE'
        }