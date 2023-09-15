from django.contrib import admin
from .models import customs

@admin.register(customs)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'size', 'color', 'material', 'properties', 'paid',
                    'created', 'updated']

    list_filter = ['paid', 'created', 'updated']
