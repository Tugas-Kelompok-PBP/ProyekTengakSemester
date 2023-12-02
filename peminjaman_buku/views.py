from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import PinjamBuku
from book.models import Book
from ulasan.models import UserReview
from django.contrib.auth.decorators import login_required
import datetime  
from django.shortcuts import render, redirect, get_object_or_404

@login_required
def pinjam_buku(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user = request.user

    sudah_dipinjam = PinjamBuku.objects.filter(pengguna=user, buku=book.title).exists()

    if sudah_dipinjam:
        response_data = {'success': False, 'message': 'Anda sudah meminjam buku ini.'}
    else:
        book = Book.objects.get(id=book_id)

        today = datetime.date.today()
        tanggal_pengembalian = today + datetime.timedelta(days=2)

        pinjaman = PinjamBuku(pengguna=request.user, buku=book.title, tanggal_peminjaman=today, tanggal_pengembalian=tanggal_pengembalian)
        pinjaman.save()

        response_data = {'success': True}
    

    return JsonResponse(response_data)


def kembalikan_buku(request, pinjam_buku_id):
    try:
        pinjam_buku = get_object_or_404(PinjamBuku, id=pinjam_buku_id)

        if pinjam_buku.buku:
            pinjam_buku.ketersediaan = 'tersedia'
            pinjam_buku.save()

        pinjam_buku.delete()

        return redirect('peminjaman_buku:pinjam_buku_list') 

    except PinjamBuku.DoesNotExist:
        return render(request, 'book_return_error.html', {'error_message': 'Peminjaman tidak ditemukan'})  


def pinjam_buku_list(request):
    borrowed_books = PinjamBuku.objects.filter(pengguna=request.user)

    context = {
        'borrowed_books': borrowed_books,
    }

    return render(request, 'pinjam_buku_list.html', context)

def show_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'detail_buku.html', {'book': book})