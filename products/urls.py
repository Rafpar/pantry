from django.urls import path

from . import views

urlpatterns = [
    path('product', views.save_product, name='product'),
    path('product/edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('product/edit/<int:product_id>/subtract/', views.edit_product, name='edit_product_subtract'),
    path('shopping_list', views.shopping_list, name='shopping_list'),
]
