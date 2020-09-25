from django.contrib import messages
from django.shortcuts import render, redirect

from products.models import Product


def product(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        user_id = request.user.id
        is_base_product = False
        if 'is_base_product' in request.POST:
            is_base_product = request.POST['is_base_product']
        is_optional_product = False
        if 'is_optional_product' in request.POST:
            is_optional_product = request.POST['is_optional_product']
        is_custom_product = False
        if 'is_custom_product' in request.POST:
            is_custom_product = request.POST['is_custom_product']
        #product_img = request.POST['product_img']
        desired_amount = request.POST['desired_amount']
        product_lists = {'is_base_product': is_base_product,
                        'is_optional_product': is_optional_product,
                        'is_custom_product': is_custom_product}

        product_list_names = calculate_product_list_names(product_lists)
        product = Product(product_name=product_name, user_id=user_id, is_base_product=is_base_product,
                          is_optional_product=is_optional_product, is_custom_product=is_custom_product,
                          desired_amount=desired_amount)
        if is_product_on_any_product_list(product_lists):
            product.save()
            messages.success(request, 'You have added new product to ' + product_list_names)
        else:
            messages.error(request, 'Please check at least one product list')
        return redirect('dashboard')


def calculate_product_list_names(product_lists):
    product_list_names = []
    if product_lists['is_base_product']:
        product_list_names.append("Base Products")
    if product_lists['is_optional_product']:
        product_list_names.append(" Optional Products")
    if product_lists['is_custom_product']:
        product_list_names.append(" Custom Products")
    return ','.join(product_list_names)


def is_product_on_any_product_list(product_lists):
    true_count = 0
    for product_list, v in product_lists:
        if product_list[v]:
            true_count += 1
    return True if true_count > 0 else False
