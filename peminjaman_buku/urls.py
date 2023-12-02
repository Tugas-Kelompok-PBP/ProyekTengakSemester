from django.urls import path
from . import views

app_name = 'peminjaman_buku' 

urlpatterns = [
    path('pinjam-buku/<int:book_id>/', views.pinjam_buku, name='pinjam_buku'),
    path('pinjam-buku-list/', views.pinjam_buku_list, name='pinjam_buku_list'),
    path('show-detail/<int:book_id>/', views.show_detail, name='show_detail'),
    path('kembalikan_buku/<int:pinjam_buku_id>/', views.kembalikan_buku, name='kembalikan_buku'),


]
