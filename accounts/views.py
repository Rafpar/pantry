from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth

from products.models import Product
from products.products_query import get_products_for


def signup(request):
    if request.method == "POST":
        valid = validate_signup_form(request)
        if not valid:
            return redirect('index')
        else:
            return save_user(request)
    else:
        return render(request, 'pages/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('index')
    else:
        return render(request, 'pages/index.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def dashboard(request):

    products = get_products_for(request.user.id)
    use_as_default_tab = True

    context = {
        'base_products': products['base_products'],
        'optional_products': products['optional_products'],
        'custom_products': products['custom_products'],
        'use_as_default_tab': use_as_default_tab
    }
    return render(request, 'accounts/dashboard.html', context)


def validate_signup_form(request):
    valid = True
    # Get from values
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
        # Check username
        if User.objects.filter(username=username).exists():
            messages.error(request, 'That username is taken')
            valid = False
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email being used')
                valid = False
    else:
        messages.error(request, 'Passwords do not match')
        valid = False
    return valid


def save_user(request):
    # Get from values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username=username, password=password,
                                    email=email, first_name=first_name,
                                    last_name=last_name)
    user.save()
    # Login after register
    auth.login(request, user)
    messages.success(request, 'You are now logged in')
    return redirect('dashboard')


def account_info(request):
    if request.method == "GET":
        user = User.objects.get(username__exact=request.user.username)
        context = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
        return render(request, 'accounts/account_info.html', context)


def delete_account(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        user_id = user.id
        user.delete()
        user_products = Product.objects.all().filter(user_id=user_id)
        user_products.delete()
        auth.logout(request)
        messages.success(request, 'Account has been removed')
        return redirect('index')


def change_password(request):
    user = User.objects.get(username__exact=request.user.username)
    if request.method == "POST":
        if is_password_form_valid(request, user):
            user.set_password(request.POST['new_password'])
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password has been successfully changed!')
        return redirect('account_info')


def is_password_form_valid(request, user):
    valid = False
    email = request.POST['email']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']
    if email == user.email:
        if new_password == confirm_password:
            valid = True
        else:
            messages.error(request, 'Passwords do not match')
    else:
        messages.error(request, 'Incorrect email!')
    return valid


