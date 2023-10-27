from django.urls import path
from customer_service.views import *

app_name = 'customer_service'

urlpatterns = [
    path('', show_customer_service, name='show_customer_service'),
]