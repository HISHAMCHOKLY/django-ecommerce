import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from datetime import date
import json
from django.contrib.postgres.search import SearchVector
from django.core.mail import send_mail
from .models import Products
from .models import Reviews
from .models import Cart
from .models import Orders
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user')
            return redirect('login')    

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')




def product(request):
    datas=Products.objects.all()
    cart=Cart.objects.all().order_by('id') 
    total=0
    cart_qty=0
    for item in cart:
        total+=item.p_price*item.qty
        cart_qty+=item.qty


    return render(request,'home.html',{'datas':datas,'cart':cart,'total':total,'cart_qty':cart_qty}) 
def cartPage(request):
    cart=Cart.objects.all().order_by('id') 
    total=0
    cart_qty=0
    for item in cart:
        total+=item.p_price*item.qty
        cart_qty+=item.qty
    return render(request,'cart.html',{'cart':cart,'total':total,'cart_qty':cart_qty})
def myorders(request):
    cart=Cart.objects.all().order_by('id') 
    orders=Orders.objects.filter(status='new').order_by('-id')
    cart_qty=0
    for item in cart:
        cart_qty+=item.qty
    return render(request,'myorders.html',{'orders':orders,'cart_qty':cart_qty})

def searchItem(request):
    search=request.POST['search']
    p=Products.objects.filter(p_name__contains=search)
    products=[]
    for x in p:
        products.append(
            {
                'id':x.id,
                'p_img_url':x.p_img.url,
                'p_name':x.p_name,
                'p_price':x.p_price,
                'slug':x.slug
            }
        )
    products = json.dumps(products,cls=DjangoJSONEncoder)
    return HttpResponse(products, content_type="text/json-comment-filtered")   


def sortItem(request):
    brand=request.POST['brand']
    category=request.POST['category']
    if  category=='all':
        p=Products.objects.filter(p_brand=brand)
        products=[]
        for x in p:
            products.append(
                {
                    'id':x.id,
                    'p_img_url':x.p_img.url,
                    'p_name':x.p_name,
                    'p_price':x.p_price,
                    'slug':x.slug
                }
            )
        products = json.dumps(products,cls=DjangoJSONEncoder)
        return HttpResponse(products, content_type="text/json-comment-filtered")  
    elif brand=='all':
        p=Products.objects.filter(p_category=category)
        products=[]
        for x in p:
            products.append(
                {
                    'id':x.id,
                    'p_img_url':x.p_img.url,
                    'p_name':x.p_name,
                    'p_price':x.p_price,
                    'slug':x.slug
                }
            )
        products = json.dumps(products,cls=DjangoJSONEncoder)
        return HttpResponse(products, content_type="text/json-comment-filtered")

    elif brand=='all' and category=='all':
        p=Products.objects.all()
        products=[]
        for x in p:
            products.append(
                {
                    'id':x.id,
                    'p_img_url':x.p_img.url,
                    'p_name':x.p_name,
                    'p_price':x.p_price,
                    'slug':x.slug
                }
            )
        products = json.dumps(products,cls=DjangoJSONEncoder)
        return HttpResponse(products, content_type="text/json-comment-filtered")
    elif brand=='all' and category=='all':
        p=Products.objects.all()
        products=[]
        for x in p:
            products.append(
                {
                    'id':x.id,
                    'p_img_url':x.p_img.url,
                    'p_name':x.p_name,
                    'p_price':x.p_price,
                    'slug':x.slug
                }
            )
        products = json.dumps(products,cls=DjangoJSONEncoder)
        return HttpResponse(products, content_type="text/json-comment-filtered")
    else:

        p=Products.objects.filter(p_category=category,p_brand=brand)
        products=[]
        for x in p:
            products.append(
                {
                    'id':x.id,
                    'p_img_url':x.p_img.url,
                    'p_name':x.p_name,
                    'p_price':x.p_price,
                    'slug':x.slug
                }
            )
        products = json.dumps(products,cls=DjangoJSONEncoder)
        return HttpResponse(products, content_type="text/json-comment-filtered")

        
         
        




def cancelOrder(request):
    if request.method == 'POST':
        id=int(request.POST.get('id'))
        c_order=Orders.objects.get(id=id)
        c_order.status='cancel'
        c_order.save()
        orders_list=[]
        orders=Orders.objects.filter(status='new').order_by('-id')
        for x in orders:
            orders_list.append({
                'id':x.id,
                'p_id':x.p_id,
                'p_img_url':x.p_img_url,
                'p_name':x.p_name,
                'p_date':x.p_date,
                'p_price':x.p_price,
                'p_qty':x.p_qty,
                'p_total':x.p_total
            })  
        orders_list = json.dumps(orders_list,cls=DjangoJSONEncoder)
        return HttpResponse(orders_list, content_type="text/json-comment-filtered")   


def item(request,slug):
    data=Products.objects.get(slug=slug)
    reviews=Reviews.objects.filter(p_id=data.id)
    cart=Cart.objects.all()
    cart_qty=0
    for item in cart:
        cart_qty+=item.qty
    return render(request,'product.html',{'data':data,'reviews':reviews,'cart_qty':cart_qty})   

def savereview(request,slug):
    if request.method == 'POST':
        product=Products.objects.get(slug=slug)
        reviw=request.POST['text']
        rating=request.POST['st']
        send_mail('REVIEW OF  PRODUCT',reviw,'chisham.c95@gmail.com',['hisham.c95@gmail.com'])
        t=Reviews(p_id=product.id,p_review=reviw,p_rating=rating)
        t.save()
        return redirect('/item/'+slug+'/')      
def addToCart(request):
    if request.method == 'POST':
        prd_id=int(request.POST.get('p_id'))
        check_Product= Products.objects.get(id=prd_id)  
        if check_Product:
            if(Cart.objects.filter(p_id=prd_id).exists()):
                cart=Cart.objects.get(p_id=prd_id)
                cart.qty+=1
                cart.save() 
                cart_list=[]
                allCart=Cart.objects.all().order_by('id')
                for item in allCart:
                    cart_list.append(
                        {
                            'id':item.id,
                            'p_id':item.p_id.id,
                            'p_img':item.p_img.url,
                            'p_name':item.p_name,
                            'p_price':item.p_price,
                            'qty':item.qty

                        }
                    )
      
                # return JsonResponse(cart_list,safe=False)  

                cart_list = json.dumps(cart_list)

                return HttpResponse(cart_list, content_type="text/json-comment-filtered")   
            else:
                c=Cart(p_id=check_Product,qty=1)
                c.save()
                cart=Cart.objects.all()
                cart_list=[]
                for item in cart:
                    cart_list.append(
                        {
                            'id':item.id,
                            'p_id':item.p_id.id,
                            'p_img':item.p_img.url,
                            'p_name':item.p_name,
                            'p_price':item.p_price,
                            'qty':item.qty

                        }
                    )
      
                # return JsonResponse(cart_list,safe=False)  

                cart_list = json.dumps(cart_list)

                return HttpResponse(cart_list, content_type="text/json-comment-filtered")          

        else:
            return JsonResponse({'status':'not exist'})            


def cartDec(request):
    if request.method == 'POST':
        prd_id=int(request.POST.get('p_id'))
        cart_item=Cart.objects.get(p_id=prd_id)
        if cart_item.qty==1:
            cart_item.delete()
            print(cart_item.p_price)
            return JsonResponse({'status':'deleted'})
        else:
            cart_item.qty-=1   
            cart_item.save()

            item ={
                "p_id":cart_item.p_id.id,
                "qty":cart_item.qty,
                "price":cart_item.p_price
            }
            item=json.dumps(item)
            return HttpResponse(item, content_type="text/json-comment-filtered")          
         

def cartAsc(request):
    if request.method == 'POST':
        prd_id=int(request.POST.get('p_id'))
        cart_item=Cart.objects.get(p_id=prd_id)
        print(cart_item.qty)
        cart_item.qty+=1
        cart_item.save()
        item ={
                "p_id":cart_item.p_id.id,
                "qty":cart_item.qty,
                "price":cart_item.p_price
            }
        item=json.dumps(item)
        return HttpResponse(item, content_type="text/json-comment-filtered")


def order(request):
    today = date.today()
    cart=Cart.objects.all()
    for x in cart:
        o=Orders(p_id=x.p_id.id,p_name=x.p_name,p_img_url=x.p_img.url,p_price=x.p_price,p_date=today,p_qty=x.qty,p_total=x.qty*x.p_price)
        o.save()
        x.delete()

    return redirect('/cart') 