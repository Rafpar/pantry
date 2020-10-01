from products.models import Product


def get_products_for(user_id):
    base_products = Product.objects.all().filter(user_id=user_id, is_base_product=True).order_by('product_name')
    optional_products = Product.objects.all().filter(user_id=user_id, is_optional_product=True).order_by('product_name')
    custom_products = Product.objects.all().filter(user_id=user_id, is_custom_product=True).order_by('product_name')
    return {
        'base_products': base_products,
        'optional_products': optional_products,
        'custom_products': custom_products
    }
