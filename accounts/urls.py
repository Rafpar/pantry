from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('account_info', views.account_info, name='account_info'),
    path('delete_account', views.delete_account, name='delete_account'),
    path('change_password', views.change_password, name='change_password')
]