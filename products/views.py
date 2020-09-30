from django.contrib import messages
from django.shortcuts import render, redirect

from products.models import Product
from products.products_query import get_products_for


def product(request):
    if request.method == 'POST':
        product_specification = calculate_product_specification(request)
        product_list_names = calculate_product_list_names(product_specification)

        product = Product(product_name=product_specification['product_name'],
                          user_id=product_specification['user_id'],
                          is_base_product=product_specification['is_base_product'],
                          is_optional_product=product_specification['is_optional_product'],
                          is_custom_product=product_specification['is_custom_product'],
                          desired_amount=product_specification['desired_amount'],
                          current_amount=product_specification['current_amount'],
                          lacking_amount=product_specification['lacking_amount'])

        products = get_products_for(request.user.id)

        if is_product_assigned_to_any_product_list(product_specification):
            product.save()
            messages.success(request, 'You have added new product to ' + product_list_names)
        else:
            messages.error(request, 'Please specify at least one product list')

        use_as_default_tab = True if not is_product_assigned_to_any_product_list(product_specification) else False

        context = {
            'base_products': products['base_products'],
            'optional_products': products['optional_products'],
            'custom_products': products['custom_products'],
            'base_product_active': product_specification['is_base_product'],
            'optional_product_active': product_specification['is_optional_product'],
            'custom_product_active': product_specification['is_custom_product'],
            'use_as_default_tab': use_as_default_tab
        }
        return render(request, 'accounts/dashboard.html', context)


def calculate_product_specification(request):
    is_base_product = False
    if 'is_base_product' in request.POST:
        is_base_product = request.POST['is_base_product']
    is_optional_product = False
    if 'is_optional_product' in request.POST:
        is_optional_product = request.POST['is_optional_product']
    is_custom_product = False
    if 'is_custom_product' in request.POST:
        is_custom_product = request.POST['is_custom_product']
    # product_img = request.POST['product_img']
    desired_amount = request.POST['desired_amount']
    current_amount = request.POST['current_amount']
    lacking_amount = int(desired_amount) - int(current_amount) if int(current_amount) < int(desired_amount) else 0
    product_specification = {
        'user_id': request.user.id,
        'product_name': request.POST['product_name'],
        'is_base_product': is_base_product,
        'is_optional_product': is_optional_product,
        'is_custom_product': is_custom_product,
        'desired_amount': desired_amount,
        'current_amount': current_amount,
        'lacking_amount': lacking_amount
    }
    return product_specification


def calculate_product_list_names(product_lists):
    product_list_names = []
    if product_lists['is_base_product']:
        product_list_names.append("Base Products")
    if product_lists['is_optional_product']:
        product_list_names.append(" Optional Products")
    if product_lists['is_custom_product']:
        product_list_names.append(" Custom Products")
    return ','.join(product_list_names)


def is_product_assigned_to_any_product_list(product_specification):
    product_lists = {'is_base_product': product_specification['is_base_product'],
                     'is_optional_product': product_specification['is_optional_product'],
                     'is_custom_product': product_specification['is_custom_product']}
    true_count = 0
    for key, value in product_lists.items():
        if value:
            true_count += 1
    return True if true_count > 0 else False
