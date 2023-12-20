import datetime
import json
from book.models import Book
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
    context = {'borrowed': Book.objects.all()}
    return render(request, "customer_service.html", context)

@login_required(login_url='/login')
def show_customer_servicer(request):
    return render(request, "customer_servicer.html", {})

def get_all_reports_json(request):
    reports = Report.objects.all()
    return HttpResponse(serializers.serialize('json', reports))

def get_reports_json(request):
    reports = Report.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', reports))

def get_book(request):
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
def add_report_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_report = Report.objects.create(
            user = request.user,
            losts = json.dumps(data.get('losts', [])),
            brokens = json.dumps(data.get('brokens', [])),
            status = 'REQUESTED',
            message = 'Diajukan'
        )
        new_report.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def confirm_report(request):
    if request.method == 'POST':
        report = Report.objects.get(pk=request.GET.get("id"))
        report.status = 'CONFIRMED'
        report.message = 'Dikonformasi, menunggu pembayaran denda'
        report.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def confirm_report_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        report = Report.objects.get(pk=data.get("id"))
        report.status = 'CONFIRMED'
        report.message = 'Dikonformasi, menunggu pembayaran denda'
        report.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def finish_report(request):
    if request.method == 'POST':
        report = Report.objects.get(pk=request.GET.get("id"))
        report.status = 'DONE'
        report.message = 'Laporan selesai'
        report.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def finish_report_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        report = Report.objects.get(pk=data.get("id"))
        report.status = 'DONE'
        report.message = 'Laporan selesai'
        report.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def add_complaint(request):
    if request.method == 'POST':
        user = request.user
        description = request.GET.get("description")
        new_complaint = Complaint(user=user, description=description)
        new_complaint.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def add_complaint_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_complain = Complaint.objects.create(
            user = request.user,
            description = data.get("description")
        )
        new_complain.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def read_complaint(request):
    if request.method == 'POST':
        complaint = Complaint.objects.get(pk=request.GET.get("id"))
        complaint.isRead = True
        complaint.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def read_complaint_flutter(request):
    if request.method == 'POST':
        complaint = Complaint.objects.get(pk=json.loads(request.body).get("id"))
        complaint.isRead = True
        complaint.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

def get_user(request):
    if request.method == "POST":
        user = get_object_or_404(User, id=request.GET.get("id"))
        return HttpResponse(serializers.serialize('json', user))
    return HttpResponseNotFound()

def show_json(request):
    data = Report.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_complaint_json(request):
    data = Complaint.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_user(request):
    data = Report.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_user_json(request):
    users = User.objects.all()
    return HttpResponse(serializers.serialize("json", users), content_type="application/json")