from django.urls import path
from fitur_premium.views import get_ruangan_json, show_main, index_premium, get_buku_premium, baca, add_sewa_buku_ajax
app_name = 'fitur_premium'

urlpatterns = [
    path('', index_premium, name='index_premium'),
    path('sewa-buku-ajax/', add_sewa_buku_ajax, name='add_sewa_buku'),
    path('sewa_ruangan', show_main, name="show_main"),
    path("get_buku_premium/", get_buku_premium, name="get_buku_premium"),
    path("baca/<int:id>", baca, name="baca"),
    path("get_ruangan_json/", get_ruangan_json, name="get_ruangan_json")
]