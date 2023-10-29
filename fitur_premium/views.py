from django.shortcuts import render
from sistem_manajemen.models import Ruangan
from book.models import Book
from fitur_premium.models import fitur_premium
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound

# Create your views here.
def get_ruangan_json(request):
    book = Ruangan.objects.filter(ketersediaan="tersedia")
    return HttpResponse(serializers.serialize('json', book))

def get_buku_premium(request):
    book = Book.objects.filter(vip="vip")
    return HttpResponse(serializers.serialize('json', book))

def baca(request,id):
    book = Book.objects.get(id=id)
    return render(request,'baca.html',{'book' : book})


def show_main(request):
    context = {
    }
    return render(request, "sewa_ruangan.html", context)

def index_premium(request):
    data_ruangan = Ruangan.objects.all()
    for dr in  data_ruangan:
        print(data_ruangan)
    return render(request,'index_premium.html',{'ruangan' : data_ruangan})    

@csrf_exempt
def add_sewa_buku_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        jumlah_hari = request.POST.get("jumlah_hari")

        new_sewa_buku = fitur_premium(title=title, jumlah_hari=jumlah_hari)
        new_sewa_buku.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()  