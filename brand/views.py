from django.shortcuts import render
from .models import Brands
from products.models import Products,Cart


# Create your views here.

def brand(request):
    datas=Brands.objects.all()
    return render(request,'brands.html',{'datas':datas})

def items(request,brand_name):
    datas=Products.objects.filter(p_brand=brand_name)
    cart=Cart.objects.all()
    total=0
    cart_qty=0
    for item in cart:
        total+=item.p_price*item.qty
        cart_qty+=item.qty
    return render(request,'home.html',{'datas':datas,'cart':cart,'total':total,'cart_qty':cart_qty})     