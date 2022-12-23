from django.shortcuts import render
import json
from jsonview.decorators import json_view
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import BrandForm,CategoryForm,PoductForm
from products.models import Products
from brand.models import Brands
from category.models import Categories
from django.template.context_processors import csrf
from django.core.files.storage import FileSystemStorage

# Create your views here.

def ecomHome(request):
    if(request.user.is_anonymous):
        return HttpResponseRedirect('/login')
    else:
        datas=Products.objects.all()
        if request.method=='POST':
            form=PoductForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/ecomAdmin')
        else:
            form=PoductForm
        return render(request,'adminProductsPage.html',{'form':form,'datas':datas})

@json_view
def addProduct(request):
    if request.method=='POST':
        p_name=request.POST.get('p_name')
        p_category=request.POST.get('p_category')
        p_brand=request.POST.get('p_brand')
        file=request.FILES['file']
        p_des=request.POST.get('p_des')
        p_price=request.POST.get('p_price')
        
        fss=FileSystemStorage()
        filename=fss.save(file.name,file)
        url=fss.url(filename)

        p=Products(p_name=p_name,p_category=p_category,p_brand=p_brand,p_img=file,p_des=p_des,p_price=p_price)
        p.save()

        products=Products.objects.all().order_by('id')

        products_list=[]
        for x in products:
            products_list.append(
                {
                    'id':x.id,
                    'p_img_url':x.p_img.url,
                    'p_name':x.p_name,
                    'p_price':x.p_price
                    
                }
            )
        products_list=json.dumps(products_list)
        return HttpResponse(products_list, content_type="text/json-comment-filtered")   
           
   

def ecomBrand(request):
    datas=Brands.objects.all()
    submitted=False
    if request.method=='POST':
        form=BrandForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ecomAdmin/brand?submitted=True')
    else:
        form=BrandForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'adminBrandPage.html',{'form':form,'submitted':submitted,'datas':datas})

def ecomCategory(request):
    datas=Categories.objects.all()
    submitted=False
    if request.method=='POST':
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ecomAdmin/category?submitted=True')
    else:
        form=CategoryForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'admincategoryPage.html',{'form':form,'submitted':submitted,'datas':datas})    


def Prd_delete(request, id):
  member = Products.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('ecomHome'))

def bnd_delete(request, id):
  member = Brands.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('ecomBrand'))

def cgy_delete(request, id):
  member = Categories.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('ecomCategory'))  


def ecomBrandAdd(request):
    submitted=False
    if request.method=='POST':
        form=BrandForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ecomAdmin/brand?submitted=True')
    else:
        form=BrandForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'adminBrandAddPage.html',{'form':form,'submitted':submitted})



