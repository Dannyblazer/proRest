from django.urls import path
from catalog.views import *

urlpatterns = [
    path('products/', ProductList.as_view(), name='product_list'),
]