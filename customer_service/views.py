import datetime
import json
from book.models import Book
#from beranda.models import User
from customer_service.models import BookReport, RoomReport, Complaint
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from itertools import chain #Combining Different Models

# @login_required(login_url='/login')
def show_customer_service(request):
    reports = BookReport.objects.filter(user=request.user)
    return render(request, "customer_service.html", reports)

def show_customer_servicer(request):
    reports = BookReport.objects.all()

def get_reports_json(request):
    reports = Book.filter()
    return HttpResponse(serializers.serialize('json', reports))

def get_borrows_json(request):
    reports = Book.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', reports))

@csrf_exempt
def add_report(request):
    if request.method == 'POST':
        user = request.user
        losts = json.loads(request.POST.get('losts', '[]'))
        brokens = json.loads(request.POST.get('brokens', '[]'))
        status = 'UNDONE'
        message = 'Laporan diajukan'
        new_report = BookReport(user=user, losts=losts, brokens=brokens, status=status, message=message)
        new_report.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def add_complaint(request):
    if request.method == 'POST':
        user = request.user
        description = request.POST.get("description")
        new_complaint = Complaint(user=user, description=description)
        new_complaint.save()