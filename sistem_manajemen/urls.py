from django.urls import path
from sistem_manajemen.views import show_sistem, get_ruangan_json, add_ruangan_ajax, show_sistem_ruangan, show_sistem_buku, get_buku_json, ganti_status_ketersediaan

app_name = 'sistem_manajemen'

urlpatterns = [
    path("", show_sistem, name="show_sistem"),
    path('get-ruangan/', get_ruangan_json, name='get_ruangan_json'),
    path('create-ruangan-ajax/', add_ruangan_ajax, name='add_ruangan_ajax'),
    path('sistem_ruangan', show_sistem_ruangan, name="sistem_ruangan"),
    path('sistem_buku', show_sistem_buku, name="sistem_buku"),
    path('get_buku_json/<str:id>', get_buku_json, name="get_buku_json"),
    path('edit_ketersediaan/<int:id>', ganti_status_ketersediaan, name='edit_ketersediaan'),
]