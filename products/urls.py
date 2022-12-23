from django.urls import path
from . import views

urlpatterns = [
    path('',views.product,name='product'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('cart',views.cartPage,name='cartPage'),
    path('search',views.searchItem,name='searchItem'),
    path('sort',views.sortItem,name='sortItem'),
    path('order',views.order,name='order'),
    path('myorders',views.myorders,name='myorders'),
    path('myorders/cancel',views.cancelOrder,name='cancelOrder'),
    path('item/<str:slug>/',views.item,name='item'),
    path('item/<str:slug>/savereview',views.savereview,name='savereview'),
    path('add-to-cart',views.addToCart,name='add-to-cart'),
    path('cart-dec',views.cartDec,name='cartDec'),
    path('cart-asc',views.cartAsc,name='cartAsc')
]


