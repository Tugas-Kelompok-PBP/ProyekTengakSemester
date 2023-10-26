import datetime
from book.models import Book
from beranda.models import User
from customer_service.models import BookReport, RoomReport, Complaint
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_customer_service(request):
    reports = BookReport.objects.filter(user=request.user) + RoomReport.objects.filter(user=request.user)
    return render(request, "customer_service.html", reports)

def show_customer_servicer(request):
    reports = BookReport.objects.all() + RoomReport.objects.all()

def get_product_json(request):
    books = Book.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', books))

@csrf_exempt
def add_lost(request, id):
    if request.method == 'POST':
        user = request.user
        book_report = BookReport.objects.create(user=user)
        
        book_report.losts.set(Book.objects.filter(id__in=request.POST.getlist('status')))
        book_report.brokens.set(Book.objects.filter(id__in=request.POST.getlist('status')))

    return HttpResponseNotFound()