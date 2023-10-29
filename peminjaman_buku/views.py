from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import PinjamBuku
from book.models import Book
from django.contrib.auth.decorators import login_required
import datetime  # Import the datetime module




@login_required
def pinjam_buku(request, book_id):

    # Dapatkan buku yang ingin dipinjam berdasarkan ID
    book = Book.objects.get(id=book_id)

    today = datetime.date.today()
    tanggal_pengembalian = today + datetime.timedelta(days=2)

    # Buat catatan peminjaman buku
    pinjaman = PinjamBuku(pengguna=request.user, buku=book, tanggal_peminjaman=today, tanggal_pengembalian=tanggal_pengembalian)
    pinjaman.save()

    response_data = {'success': True}
    
    return JsonResponse(response_data)


def kembalikan_buku(request):
    context = {}
    return render(request, 'kembalikan_buku.html', context)


def pinjam_buku_list(request):
    borrowed_books = PinjamBuku.objects.filter(pengguna=request.user)

    context = {
        'borrowed_books': borrowed_books,
    }

    return render(request, 'pinjam_buku_list.html', context)

