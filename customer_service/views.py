import datetime
import json
from book.models import Book
from book.views import get_books
#from beranda.models import User
#from peminjaman_buku.models import PinjamBuku
from customer_service.models import BookReport, Complaint
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from itertools import chain #Combining Different Models

@login_required(login_url='/login')
def show_customer_service(request):
    context = {'books': Book.objects.all()}
    return render(request, "customer_service.html", context)

def show_customer_servicer(request):
    reports = BookReport.objects.all()

def get_reports_json(request):
    reports = BookReport.objects.all()
    return HttpResponse(serializers.serialize('json', reports))

def get_books_json_by_ids(request, ids):
    books = Book.objects.filter(pk__in=ids)
    return HttpResponse(serializers.serialize('json', books))

def get_borrows_json(request):
    reports = Book.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', reports))

@csrf_exempt
def add_report(request):
    if request.method == 'POST':
        user = request.user
        data = json.loads(request.body)
        losts = json.dumps(data.get('losts', []))
        brokens = json.dumps(data.get('brokens', []))
        status = 'UNDONE'
        message = 'Laporan diajukan'
        new_report = BookReport(user=user, status=status, message=message)
        new_report.set_losts(losts)
        new_report.set_brokens(brokens)
        new_report.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def add_complaint(request):
    if request.method == 'POST':
        user = request.user
        description = request.POST.get("description")
        new_complaint = Complaint(user=user, description=description)
        new_complaint.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def show_json(request):
    data = BookReport.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")