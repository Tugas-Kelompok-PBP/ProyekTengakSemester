from django.urls import path
from .views import show_ulasan, get_reviews_json, add_review_ajax

app_name = 'ulasan'

urlpatterns = [
    path('', show_ulasan, name='show_ulasan'),
    path('reviews-json/<int:book_id>/', get_reviews_json, name='get_reviews_json'),
    path('add-review/<int:book_id>/', add_review_ajax, name='add_review_ajax'),
]
