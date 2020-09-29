from django.contrib import auth
from django.shortcuts import render, redirect


def index(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return render(request, 'pages/index.html')
    else:
        return redirect('dashboard')


def about(request):
    return render(request, 'pages/about.html')

