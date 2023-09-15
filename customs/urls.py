from django.urls import path
from . import views

app_name = 'customs'

urlpatterns = [
    path('', views.custom_order_create, name='custom_order_create'),

]