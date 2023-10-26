from django.shortcuts import render
from sistem_manajemen.models import Ruangan
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def get_ruangan_json(request):
    book = Ruangan.objects.filter(ketersediaan="tersedia")
    return HttpResponse(serializers.serialize('json', book))

def show_main(request):
    context = {
    }
    return render(request, "sewa_ruangan.html", context)