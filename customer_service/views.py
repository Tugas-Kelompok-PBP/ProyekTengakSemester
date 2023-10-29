import datetime
import json
from book.models import Book
from peminjaman_buku.models import PinjamBuku
from customer_service.models import Report, Complaint
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@login_required(login_url='/login')
def show_customer_service(request):
    context = {'borrowed': PinjamBuku.objects.filter(pengguna=request.user)}
    return render(request, "customer_service.html", context)

def show_customer_servicer(request):
    return render(request, "customer_servicer.html", {})

def get_all_reports_json(request):
    reports = Report.objects.all()
    return HttpResponse(serializers.serialize('json', reports))

def get_reports_json(request):
    reports = Report.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', reports))

def get_books_json_by_ids(request, ids):
    books = Book.objects.filter(pk__in=ids)
    return HttpResponse(serializers.serialize('json', books))

@csrf_exempt
def add_report(request):
    if request.method == 'POST':
        user = request.user
        data = json.loads(request.body)
        losts = data.get('losts', [])
        brokens = data.get('brokens', [])
        status = 'REQUESTED'
        message = 'Diajukan'
        new_report = Report(user=user, status=status, message=message)
        new_report.set_losts(losts)
        new_report.set_brokens(brokens)
        new_report.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def confirm_report(request, id):
    if request.method == 'POST':
        report = Report.objects.filter(pk=id)
        report.set_status('CONFIRMED')
        report.set_message('Dikonformasi, menunggu pembayaran denda')
        report.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def finish_report(request, id):
    if request.method == 'POST':
        report = Report.objects.filter(pk=id)
        report.set_status('DONE')
        report.set_message('Laporan selesai')
        report.save()
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
    data = Report.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")