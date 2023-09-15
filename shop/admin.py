from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'size', 'mass', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available'] #дает возможность редактировать поля на сайте администрирования
    prepopulated_fields = {'slug': ('name',)} #помним, что атрибут prepopulated_fields
    # используется для того, чтoбы указывать поля, значение которых устанавливается
    # автоматически с использованием значения других полей. Как вы уже убедились, это удобно для генерирования слагов.

