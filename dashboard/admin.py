from django.contrib import admin
from .models import User, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'age', 'gender', 'city', 'country', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'city', 'country')
    list_filter = ('gender', 'country', 'state')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user_id', 'status', 'gender', 'created_at', 'returned_at', 'shipped_at', 'delivered_at', 'num_of_item')
    search_fields = ('order_id', 'status', 'gender')
    list_filter = ('status', 'gender')
