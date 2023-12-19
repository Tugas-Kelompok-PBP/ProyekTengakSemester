from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User

# Create your views here.
@csrf_exempt
def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse({
                "message": "Berhasil login",
                "username": user.username,
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal"
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    
@csrf_exempt
def logout_user(request):
    try:
        logout(request)
        return JsonResponse({
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        # print(request.body)
        data = json.loads(request.body)

        username = data["username"]
        password1 = data["password1"]
        password2 = data["password2"]

        if password1 != password2:
            return JsonResponse({'status': 'failed', 'message': 'Pasword Tidak Sama'})

        new_user = User.objects.create_user(username = username, password = password1)
        new_user.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

# @csrf_exempt
# def register(request):
#     form = UserCreationForm()
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({
#                 "message": "Akun berhasil dibuat",
#             }, status=200)
#         else:
#             return JsonResponse({
#                 "status": False,
#                 "message": "Akun gagal dibuat"
#             }, status=401)
#     else:
#          return JsonResponse({
#             "status": False,
#             "message": "Akun gagal dibuat"
#         }, status=401)