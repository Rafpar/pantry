from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from products.models import Product
from products.products_query import get_products_for, get_base_products_for, get_optional_products_for, \
    get_custom_products_for


def save_product(request):
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


def shopping_list(request):
    product_lists = {}
    if request.method == 'GET':
        if 'is_base_product' in request.GET:
            base_products = get_base_products_for(request.user.id)
            product_lists['Base products'] = base_products
        if 'is_optional_product' in request.GET:
            optional_products = get_optional_products_for(request.user.id)
            product_lists['Optional products'] = optional_products
        if 'is_custom_product' in request.GET:
            custom_products = get_custom_products_for(request.user.id)
            product_lists['Custom products'] = custom_products

        context = {'product_lists': product_lists}
        return render(request, 'pages/shopping_list.html', context)


def edit_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        if 'subtract' in request.path:
            product.current_amount -= 1
        else:
            product.current_amount = request.POST['current_amount']
            product.desired_amount = request.POST['desired_amount']
        product.lacking_amount = calculate_lacking_amount_from(product.current_amount, product.desired_amount)
        product.save()
    products = get_products_for(request.user.id)
    context = {
        'base_products': products['base_products'],
        'optional_products': products['optional_products'],
        'custom_products': products['custom_products'],
        'base_product_active': True if 'is_base_product' in request.POST else False,
        'optional_product_active': True if 'is_optional_product' in request.POST else False,
        'custom_product_active': True if 'is_custom_product' in request.POST else False
    }
    return render(request, 'accounts/dashboard.html', context)


def calculate_lacking_amount_from(current_amount, desired_amount):
    return int(desired_amount) - int(current_amount) if int(current_amount) < int(
        desired_amount) else 0


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
    product_name = None
    if 'product_name' in request.POST:
        product_name = request.POST['product_name']
    # product_img = request.POST['product_img']
    desired_amount = request.POST['desired_amount']
    current_amount = request.POST['current_amount']
    lacking_amount = calculate_lacking_amount_from(current_amount, desired_amount)
    product_specification = {
        'user_id': request.user.id,
        'product_name': product_name,
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
