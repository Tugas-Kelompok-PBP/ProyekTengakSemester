from django.urls import path
from . import views
from .views import create_pinjam_buku

app_name = 'peminjaman_buku' 

urlpatterns = [
    path('pinjam-buku/<int:book_id>/', views.pinjam_buku, name='pinjam_buku'),
    path('pinjam_buku_list/', views.pinjam_buku_list, name='pinjam_buku_list'),
    path('show-detail/<int:book_id>/', views.show_detail, name='show_detail'),
    path('kembalikan_buku/<str:pinjam_buku_title>/', views.kembalikan_buku, name='kembalikan_buku'),
    path('create_pinjam_buku/', create_pinjam_buku, name='create_pinjam_buku'),
    path('list_buku_flutter/<str:uname>/', views.list_buku_flutter, name='list_buku_flutter'),

]
