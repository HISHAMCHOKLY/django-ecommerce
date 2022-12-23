from django.urls import path
from . import views

urlpatterns = [
    path('',views.brand,name='brand'),
    path('items/<str:brand_name>',views.items,name='items'),


    # path('product/',views.product,name='product'),
    # path('brands/',views.brands,name='brands'),
    # path('categories/',views.categories,name='categories'),
    # path('brands/products/',views.products,name='products'),
    # path('categories/products/',views.products,name='products'),
    # path('brands/products/product',views.product,name='product'),
    # path('categories/products/product',views.product,name='product'),
]

