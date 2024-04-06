from django.urls import path
from . import views

urlpatterns = [
    
    path('products/', views.product_list_create, name='product-list-create'),
    path('products/<int:product_id>/', views.product_detail, name='product-detail'),
    path('customers/', views.customer_list_create, name='customer-list-create'),
    path('customers/<int:customer_id>/', views.customer_detail, name='customer-detail'),
    path('bill/', views.bill_create, name='bill-create'),
]
