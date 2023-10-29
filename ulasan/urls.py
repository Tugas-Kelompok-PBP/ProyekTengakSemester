from django.urls import path
from .views import show_ulasan, get_reviews_json, add_review_ajax, delete_review, edit_review

app_name = 'ulasan'

urlpatterns = [
    path('', show_ulasan, name='show_ulasan'),
    path('reviews-json/<int:book_id>/', get_reviews_json, name='get_reviews_json'),
    path('add-review/<int:book_id>/', add_review_ajax, name='add_review_ajax'),
    path('delete-review/<int:review_id>/', delete_review, name='delete_review'),
    path('edit-review/<int:review_id>/', edit_review, name='edit_review'),
]
