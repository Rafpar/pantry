from django.urls import path

from . import views

urlpatterns = [
    path('product', views.save_product, name='product'),
    path('product/edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('product/edit/<int:product_id>/subtract/', views.edit_product, name='edit_product_subtract'),
    path('update/current_amount/<int:product_id>', views.update_current_amount, name='update_current_amount'),
    path('shopping_list', views.shopping_list, name='shopping_list'),
    path('product/delete/<int:product_id>', views.product_delete, name='product_delete'),
]
