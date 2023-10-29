from django.urls import path
from customer_service.views import *

app_name = 'customer_service'
urlpatterns = [
    path('', show_customer_service, name='show_customer_service'),
    path('add_report/', add_report, name='add_report'),
    path('add_complaint/', add_complaint, name='add_complaint'),
    path('get_reports_json', get_reports_json, name='get_reports_json'),
    path('get_all_reports_json', get_all_reports_json, name='get_all_reports_json'),
    path('get_books_json_by_ids/', get_books_json_by_ids, name='get_books_json_by_ids'),
    path('json/', show_json, name='show_json'),
    path('confirm_report/', confirm_report, name='confirm_report'),
    path('finish_report/', finish_report, name='finish_report'),
    path('customer_servicer', show_customer_service, name='show_customer_servicer'),
]