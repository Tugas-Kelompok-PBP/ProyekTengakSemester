from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import PinjamBuku
from book.models import Book
from ulasan.models import UserReview
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.core import serializers
from datetime import datetime, timedelta

from .models import PinjamBuku

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User

@login_required
def pinjam_buku(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user = request.user

    sudah_dipinjam = PinjamBuku.objects.filter(pengguna=user, buku=book.title).exists()

    if sudah_dipinjam:
        response_data = {'success': False, 'message': 'Anda sudah meminjam buku ini.'}
    else:
        book = Book.objects.get(id=book_id)

        today = datetime.now()
        tanggal_pengembalian = datetime.now() + timedelta(days=2)

        pinjaman = PinjamBuku(pengguna=request.user, buku=book.title, tanggal_peminjaman=today, tanggal_pengembalian=tanggal_pengembalian)
        pinjaman.save()

        response_data = {'success': True}
    

    return JsonResponse(response_data)


def kembalikan_buku(request, pinjam_buku_title):
    try:
        print(pinjam_buku_title)
        print(request.path)
        pinjam_buku = PinjamBuku.objects.all()
        for pb in pinjam_buku:
            print(pb.buku + "Test")
            if pb.buku == pinjam_buku_title:
                pb.ketersediaan = 'tersedia'
                pb.save()
                pb.delete()

        return redirect('peminjaman_buku:pinjam_buku_list') 

    except PinjamBuku.DoesNotExist:
        return render(request, 'book_return_error.html', {'error_message': 'Peminjaman tidak ditemukan'})  


def pinjam_buku_list(request):
    borrowed_books = PinjamBuku.objects.filter(pengguna=request.user)

    context = {
        'borrowed_books': borrowed_books,
    }

    return render(request, 'pinjam_buku_list.html', context)

def list_buku_flutter(request, uname):
    data_item = PinjamBuku.objects.all()
    for data in data_item:
        if data.pengguna.username == uname:
            user_id = data.pengguna
            data = PinjamBuku.objects.filter(pengguna = user_id)
            break
        else:
            data = []

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'detail_buku.html', {'book': book})

@csrf_exempt
def create_pinjam_buku(request):
    date_format = "%Y-%m-%d"  

    if request.method == 'POST':

        data = json.loads(request.body)

        new_item = PinjamBuku.objects.create(
            pengguna = request.user,
            buku = data['buku'],
            tanggal_peminjaman = datetime.now(),
            tanggal_pengembalian = datetime.now() + timedelta(days=2),
        )

        new_item.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)





