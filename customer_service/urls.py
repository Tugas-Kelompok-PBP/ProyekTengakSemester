from django.urls import path
from customer_service.views import *

app_name = 'customer_service'
urlpatterns = [
    path('', show_customer_service, name='show_customer_service'),
    path('get_borrows_json/', get_borrows_json, name='get_borrows_json'),
    path('add_report/', add_report, name='add_report'),
    path('add_complaint/', add_complaint, name='add_complaint'),
    path('get_reports_json', get_reports_json, name='get_reports_json'),
    path('get_books_json_by_ids/', get_books_json_by_ids, name='get_books_json_by_ids'),
    path('json/', show_json, name='show_json'),
]