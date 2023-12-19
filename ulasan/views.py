from django.shortcuts import get_object_or_404, render,redirect
from ulasan.models import UserReview
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from book.models import Book

# Create your views here.

def show_peminjaman_buku(request):
    books = Book.objects.filter(ketersediaan='tersedia')

    context = {
        'books': books,
    }
    
    return render(request,'peminjaman_buku.html', context)


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

def get_reviews_json(request, book_id):
    reviews = UserReview.objects.filter(book_id=book_id)
    data = [{'user_name': reviews.user_name, 'rating': reviews.rating, 'review_text': reviews.review_text, 'date_added': reviews.date_added} for review in reviews]
    return JsonResponse(data, safe=False)

@login_required(login_url='/login')
def delete_review(request, review_id):
    review = get_object_or_404(UserReview, id=review_id)
    
    # Check if the user is the owner of the review or has permission to delete it
    if review.user_name == request.user.username:
        review.delete()
        return HttpResponse("Review deleted", status=200)
    else:
        return HttpResponse("Permission denied", status=403)

@login_required(login_url='/login')
def edit_review(request, review_id):
    review = get_object_or_404(UserReview, id=review_id)
    
    # Check if the user is the owner of the review or has permission to edit it
    if review.user_name == request.user.username:
        if request.method == 'POST':
            # Update the review
            review.rating = request.POST.get('rating')
            review.review_text = request.POST.get('review_text')
            review.save()
            return HttpResponse("Review updated", status=200)
        
        return render(request, 'edit_review.html', {'review': review})
    else:
        return HttpResponse("Permission denied", status=403)