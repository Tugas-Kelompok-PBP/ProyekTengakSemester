from django.urls import path
from sistem_manajemen.views import show_sistem, get_ruangan_json, add_ruangan_ajax

app_name = 'fitur_premium'

urlpatterns = [
    path("", show_sistem, name="show_sistem"),
    path('get-ruangan/', get_ruangan_json, name='get_ruangan_json'),
    path('create-ruangan-ajax/', add_ruangan_ajax, name='add_ruangan_ajax'),
]