from django.shortcuts import render,redirect
from ulasan.models import UserReview
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from book.models import Book
from django.contrib import messages  
from django.http import Http404
# Create your views here.

# @login_required(login_url='/login')
def show_ulasan(request, book_id=None):
    book = None
    reviews = None
    if book_id is not None:
        try:
            book = Book.objects.get(pk=book_id)
            reviews = UserReview.objects.filter(book=book)
        except Book.DoesNotExist:
            # Tangani jika buku tidak ditemukan
            book = None
    return render(request, "ulasan.html", {'book': book, 'reviews': reviews})

def get_reviews_json(request, book_id):
    reviews = UserReview.objects.filter(book_id=book_id)
    review_data = []
    for review in reviews:
        review_data.append({
            'user_name': review.user_name,
            'rating': review.rating,
            'review_text': review.review_text,
        })
    return HttpResponse(serializers.serialize('json', reviews))

@login_required(login_url='/login')
@csrf_exempt
def add_review_ajax(request, book_id):
    if request.method == 'POST':
        user_name = request.POST.get("user_name")
        rating = request.POST.get("rating")
        review_text = request.POST.get("review_text")

        review = UserReview(book_id=book_id, user_name=user_name, rating=rating, review_text=review_text)
        review.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()