from django.shortcuts import render
from sistem_manajemen.models import Ruangan
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from book.models import Book
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse
from sistem_manajemen.forms import RuanganForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def show_sistem(request):
    if(request.user.username.split("-")[-1] != "pekerja"):
        return HttpResponse(b"Restricted")
    context = {
        'name':request.user.username,
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def show_sistem_ruangan(request):
    if(request.user.username.split("-")[-1] != "pekerja"):
        return HttpResponse(b"Restricted")
    ruangan = Ruangan.objects.all()
    form = RuanganForm(request.POST)
    context = {
        'products':ruangan,
        'form': form,
    }
    return render(request, "sistem_manajemen.html", context)

@login_required(login_url='/login')
def show_sistem_buku(request):
    if(request.user.username.split("-")[-1] != "pekerja"):
        return HttpResponse(b"Restricted")
    context = {
    }
    return render(request, "manage_buku.html", context)

def get_buku_json(request, id):
    if(id == "tidak_ada_filter") :
        book = Book.objects.all()
    else :
        book = Book.objects.filter(genre=id)
    return HttpResponse(serializers.serialize('json', book))

def get_ruangan_json(request):
    ruangan = Ruangan.objects.all()
    return HttpResponse(serializers.serialize('json', ruangan))

@csrf_exempt
def add_ruangan_ajax(request):
    if request.method == 'POST':
        form = RuanganForm(request.POST)
        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponse(b"CREATED", status=201)
        

    return HttpResponseNotFound()

def ganti_status_ketersediaan(request, id):
    ruangan = Ruangan.objects.get(pk=id)
    if(ruangan.ketersediaan == "tersedia") :
        ruangan.ketersediaan = "disewa"
    else:
        ruangan.ketersediaan = "tersedia"
    ruangan.save()
    return HttpResponseRedirect(reverse('sistem_manajemen:sistem_ruangan'))

