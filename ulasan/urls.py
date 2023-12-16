from django.urls import path
from peminjaman_buku.views import show_detail
from .views import create_review_flutter, get_user_review, show_peminjaman_buku, get_reviews_json, add_review_ajax, show_ulasan
from django.contrib.auth.views import LoginView

app_name = 'ulasan'

urlpatterns = [
    path('detail/<int:book_id>/', show_detail, name='show_detail'),
    path('peminjaman_buku/', show_peminjaman_buku, name='show_peminjaman_buku'),
    path('show-ulasan/<int:book_id>', show_ulasan, name ='show_ulasan'),
    path('get-reviews-json/<int:book_id>/', get_reviews_json, name='get_reviews_json'),
    path('get-user-reviews/<int:id>', get_user_review, name='get_user_review'),
    path('add-review-ajax/<int:book_id>/', add_review_ajax, name='add_review_ajax'),
    path('login/', LoginView.as_view(), name='login'),
    path('create-review-flutter/<int:id>/', create_review_flutter, name='create_review_flutter'),
]
