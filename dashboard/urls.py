from django.urls import path
from . import views

urlpatterns = [
    path('load-users/', views.load_users_csv, name='load_users'),
    path('load-orders/', views.load_orders_csv, name='load_orders'),
]
