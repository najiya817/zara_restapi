from django.shortcuts import redirect, render
from .models import *
from django.views import View
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,"index.html")
@csrf_exempt
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=RegAdmin.objects.get(username=username,password=password)
            print(user)
            if user is not None:
                # login(request,user)
                return render(request,"home.html")
            else:
                return redirect('logi')
        except:
            return render(request,"log.html")
    return render(request,"log.html")

@csrf_exempt
def reg_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=RegAdmin(username=username,password=password)
        user.save()
        return render(request,"log.html")
    return render(request,"reg.html")

def LandHome(request):
    return render(request,"home.html")