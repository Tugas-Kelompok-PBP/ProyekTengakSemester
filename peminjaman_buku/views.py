from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import PinjamBuku
from book.models import Book
from ulasan.models import UserReview
from django.contrib.auth.decorators import login_required
import datetime  
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.core import serializers

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

        today = datetime.date.today()
        tanggal_pengembalian = today + datetime.timedelta(days=2)

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
            if pb.buku == pinjam_buku_title:
                pb.ketersediaan = 'tersedia'
                pb.save()
                print(pb.buku)
                print(pb.id)
        # pinjam_buku = get_object_or_404(PinjamBuku, id=pinjam_buku_id)
        # pinjam_buku = PinjamBuku.objects.get(buku=pinjam_buku_title)
                pb.delete()
        # print(pinjam_buku.buku)
        # print(pinjam_buku.id)
        # if pinjam_buku.buku:
        #     pinjam_buku.ketersediaan = 'tersedia'
        #     pinjam_buku.save()

        # pinjam_buku.delete()

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
    
    # print(uname)
    data_item = PinjamBuku.objects.all()
    for data in data_item:
        if data.pengguna.username == uname:
            user_id = data.pengguna
            data = PinjamBuku.objects.filter(pengguna = user_id)
            break
        else:
            data = []

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    # print(request.user)
    # pinjam = PinjamBuku.objects.filter(pengguna=request.user)
    # # pinjam = PinjamBuku.objects.all()
    # return HttpResponse(serializers.serialize('json', pinjam))
    # context = {
    #     'borrowed_books': borrowed_books,
    # }
    # return render(request, 'pinjam_buku_list.html', context)


def show_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'detail_buku.html', {'book': book})

@csrf_exempt
def create_pinjam_buku(request):
    if request.method == 'POST':
        try:
            # Mengambil data dari permintaan POST
            data = json.loads(request.body)
            username = data['username']
            buku = data['buku']
            tanggal_peminjaman = data['tanggal_peminjaman']
            tanggal_pengembalian = data['tanggal_pengembalian']

            # Mendapatkan objek User berdasarkan username
            user = User.objects.get(username=username)

            # Membuat objek PinjamBuku
            pinjam_buku = PinjamBuku.objects.create(
                pengguna=user,
                buku=buku,
                tanggal_peminjaman=tanggal_peminjaman,
                tanggal_pengembalian=tanggal_pengembalian,
                status_acc=False
            )

            return JsonResponse({'status': 'success', 'message': 'PinjamBuku created successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid method'})