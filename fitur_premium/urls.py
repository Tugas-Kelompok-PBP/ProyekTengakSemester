from django.urls import path
from fitur_premium.views import get_ruangan_json, show_main
app_name = 'fitur_premium'

urlpatterns = [
    path('sewa_ruangan', show_main, name="show_main"),
    path("get_ruangan_json/", get_ruangan_json, name="get_ruangan_json")
]