from django.shortcuts import render
from .models import Categories
from products.models import Products,Cart


# Create your views here.


def category(request):
    datas=Categories.objects.all()
    return render(request,'categories.html',{'datas':datas}) 

def items(request,category_name):
    datas=Products.objects.filter(p_category=category_name)
    cart=Cart.objects.all()
    total=0
    cart_qty=0
    for item in cart:
        total+=item.p_price*item.qty
        cart_qty+=item.qty
    return render(request,'home.html',{'datas':datas,'total':total,'cart':cart,'cart_qty':cart_qty})       