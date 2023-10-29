import datetime
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from book.models import Book

# @login_required(login_url='/login')
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('beranda:show_beranda')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('beranda:login')

def show_beranda(request):
    context = {1:1,2:2,3:3}
    return render(request, "beranda.html", context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun Anda telah berhasil dibuat!')
            return redirect('beranda:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('beranda:show_beranda'))
    context = {'form': form, 'books': Book.objects.all()}
    return render(request, "borrow.html", context)

from django.shortcuts import render

def show_peminjaman_buku(request):
    current_user = request.user.username

    # Periksa apakah pengguna adalah VIP
    if current_user.endswith('-vip'):
        books = Book.objects.filter(ketersediaan='tersedia')
    else:
        books = Book.objects.filter(ketersediaan='tersedia', vip='biasa')

    context = {
        'books': books,
    }

    return render(request, 'peminjaman_buku.html', context)
   
