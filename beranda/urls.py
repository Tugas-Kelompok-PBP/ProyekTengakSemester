from django.urls import path
from beranda.views import *

app_name = 'beranda'
urlpatterns = [
    path('', show_beranda, name='show_beranda'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('peminjaman_buku/', show_peminjaman_buku, name='show_peminjaman_buku'),


]