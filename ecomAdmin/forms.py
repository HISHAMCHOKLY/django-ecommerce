from django import forms
from django.forms import ModelForm
from products.models import Products
from brand.models import Brands
from category.models import Categories

class BrandForm(ModelForm):
    class Meta:
        model = Brands

        # this for take all value
        # fields='__all__'

        # take specific values

        fields=('b_name','b_img')

class PoductForm(ModelForm):
    class Meta:
        model = Products

        # this for take all value
        fields='__all__'
        widgets = {
            'p_name': forms.TextInput(attrs={
                'id': 'p_name', 
                'required': True 
            }),
            'p_category': forms.TextInput(attrs={
                'id': 'p_category', 
                'required': True 
            }),
            'p_brand': forms.TextInput(attrs={
                'id': 'p_brand', 
                'required': True 
            }),
            'p_img': forms.FileInput(attrs={
                'id': 'p_img', 
                'required': True 
            }),
            'p_des': forms.TextInput(attrs={
                'id': 'p_des', 
                'required': True 
            }),
            'p_price': forms.TextInput(attrs={
                'id': 'p_price', 
                'required': True 
            })


        }    

        # take specific values
class CategoryForm(ModelForm):
    class Meta:
        model = Categories

        # this for take all value
        fields=('c_name','c_img')