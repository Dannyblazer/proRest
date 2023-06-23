from django.urls import path
from catalog.views import *

urlpatterns = [
    path('products/', product_list, name='product_list'),
]