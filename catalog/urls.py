from django.urls import path
from catalog.views import *

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:product_id>/', ProductDetail.as_view(), name='product_detail'),
    path('products/<int:product_id>/reviews/', ReviewList.as_view(), name='reviews'),
    path('products/<int:product_id>/reviews/<int:review_id>/', ReviewDetail.as_view(), name='product_reviews'),
]