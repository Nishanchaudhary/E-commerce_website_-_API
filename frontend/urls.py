from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('categories/', views.category_list, name='category_list'),
    path('orders/', views.order_list, name='order_list'),
    path('add-to-order/<int:product_id>/', views.add_to_order, name='add_to_order'),
]
