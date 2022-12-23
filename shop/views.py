from django.shortcuts import render
from django.http import HttpResponse,request

# Create your views here.
def home(request):
    return render(request,'home.html')

def brands(request):
    return render(request,'brands.html')

def categories(request):
    return render(request,'categories.html')        

def products(request):
    return render(request,'home.html') 

def product(request):
    return render(request,'product.html')       