from django.shortcuts import get_object_or_404, render
from ulasan.forms import BookForm
from ulasan.models import UserReview
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from book.models import Book

# Create your views here.

def show_peminjaman_buku(request):
    books = Book.objects.filter(ketersediaan='tersedia')

    context = {
        'books': books,
    }
    
    return render(request,'peminjaman_buku.html', context)

def show_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'detail_buku.html', {'book': book})

def show_ulasan(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = UserReview.objects.filter(book=book)
    form = BookForm()

    context = {
        'page': 'Reviews',
        'reviews': reviews,
        'book': book,
        'form': form,
    }

    return render(request, "ulasan_buku.html", context)

def get_reviews_json(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = UserReview.objects.filter(book=book).values('user_name', 'rating', 'review_text', 'date_added')
    return JsonResponse(list(reviews), safe= False)

def get_user_review(request,id):
    book = Book.objects.get(pk=id)
    reviews = UserReview.objects.filter (book= book, user_name = request.user).values('user_name', 'rating', 'review_text', 'date_added')
    return JsonResponse(list(reviews), safe = False)


@csrf_exempt
def add_review_ajax(request, book_id):
    if request.method == 'POST':
        user_name = request.user.username if request.user.is_authenticated else "AnonymousUser"
        rating = request.POST.get("rating")
        review_text = request.POST.get("review_text")
        book = get_object_or_404(Book, id=book_id)

        try:
            # Memastikan nilai rating berada dalam rentang yang valid (misalnya, antara 1 dan 5)
            if rating is not None:
                rating = int(rating)
                if 1 <= rating <= 5:
                    # Proses penyimpanan ulasan ke database
                    review = UserReview.objects.create(
                        book=book,
                        user_name=user_name,
                        rating=rating,
                        review_text=review_text,
                    )
                    return HttpResponse(b"CREATED", status=201)
                else:
                    return JsonResponse({'status': 'error', 'message': 'Rating harus berada dalam rentang 1 hingga 5.'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Rating tidak boleh kosong.'})
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Rating harus berupa angka.'})
    else:
        return HttpResponseNotFound()
