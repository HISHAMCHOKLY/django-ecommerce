from django.urls import path
from . import views

urlpatterns = [
    path('',views.ecomHome,name='ecomHome'),
    path('addProduct',views.addProduct,name='addProduct'),
    path('delete/<int:id>', views.Prd_delete, name='delete'),
    path('brand',views.ecomBrand,name='ecomBrand'),
    path('brand/add',views.ecomBrandAdd,name='ecomBrand'),
    path('brand/delete/<int:id>', views.bnd_delete, name='bnd_delete'),
    path('category',views.ecomCategory,name='ecomCategory'),
    path('category/delete/<int:id>', views.cgy_delete, name='cgy_delete'),
]