from django.urls import path
from customer_service.views import *

app_name = 'customer_service'
urlpatterns = [
    path('', show_customer_service, name='show_customer_service'),
    path('customer_servicer', show_customer_servicer, name='show_customer_servicer'),
    path('add_report/', add_report, name='add_report'),
    path('add_complaint/', add_complaint, name='add_complaint'),
    path('get_reports_json', get_reports_json, name='get_reports_json'),
    path('get_all_reports_json', get_all_reports_json, name='get_all_reports_json'),
    path('get_book/', get_book, name='get_book'),
    path('json/', show_json, name='show_json'),
    path('json_by_user/', show_json_by_user, name='show_json_by_user'),
    path('complaint_json/', show_complaint_json, name='show_complaint_json'),
    path('confirm_report/', confirm_report, name='confirm_report'),
    path('finish_report/', finish_report, name='finish_report'),
    path('confirm_report_flutter/', confirm_report_flutter, name='confirm_report_flutter'),
    path('finish_report_flutter/', finish_report_flutter, name='finish_report_flutter'),
    path('get_user/', get_user, name='get_user'),
    path('user/', show_user_json, name='show_user_json'),
    path('add_report_flutter/', add_report_flutter, name='add_report_flutter'),
    path('add_complaint_flutter/', add_complaint_flutter, name='add_complaint_flutter'),
    path('read_complaint/', read_complaint, name='read_complaint'),
    path('read_complaint_flutter/', read_complaint_flutter, name='read_complaint_flutter')
]