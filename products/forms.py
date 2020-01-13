from django import forms
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
        'title',
        'description',
        'price'
        ]

class RawProductForm(forms.Form):
    title  = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"title name"}))
    description = forms.CharField(required = False, widget = forms.Textarea(
        attrs = {

        }
        ))
    price   = forms.DecimalField()
