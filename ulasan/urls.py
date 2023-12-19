from django.urls import path
from peminjaman_buku.views import show_ulasan
from .views import show_peminjaman_buku, get_reviews_json, add_review_ajax, delete_review, edit_review

app_name = 'ulasan'

urlpatterns = [
    path('ulasan/<int:book_id>/', show_ulasan, name='show_ulasan'),
    path('peminjaman_buku/', show_peminjaman_buku, name='show_peminjaman_buku'),
    path('get-reviews-json/<int:book_id>/', get_reviews_json, name='get_reviews_json'),
    path('add-review/<int:book_id>/', add_review_ajax, name='add_review_ajax'),
    path('delete-review/<int:review_id>/', delete_review, name='delete_review'),
    path('edit-review/<int:review_id>/', edit_review, name='edit_review'),
]
