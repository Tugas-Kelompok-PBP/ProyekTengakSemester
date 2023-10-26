from django.shortcuts import render
from sistem_manajemen.models import Ruangan
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from book.models import Book


# Create your views here.

def show_sistem(request):
    context = {
    }

    return render(request, "main.html", context)

def show_sistem_ruangan(request):
    context = {
    }
    return render(request, "sistem_manajemen.html", context)

def show_sistem_buku(request):
    context = {
    }
    return render(request, "manage_buku.html", context)

def get_buku_json(request):
    book = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book))

def get_ruangan_json(request):
    ruangan = Ruangan.objects.all()
    return HttpResponse(serializers.serialize('json', ruangan))

@csrf_exempt
def add_ruangan_ajax(request):
    if request.method == 'POST':
        nomor = request.POST.get("nomor")
        ketersediaan = request.POST.get("ketersediaan")

        new_product = Ruangan(nomor=nomor, ketersediaan=ketersediaan)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()