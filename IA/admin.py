from django.contrib import admin
from .models import Customers, reservations, hostels

@admin.register(Customers)
class Customer_admin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'message'
    ]
    search_fields = [
        'email'
    ]


admin.site.register(reservations)
admin.site.register(hostels)

# Register your models here