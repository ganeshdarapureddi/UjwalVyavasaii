from django.shortcuts import render
from .models import Contact,Register
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.shortcuts import redirect, render  ,HttpResponse
from django.contrib import messages   

def home_page(request):
    return render(request,'Home/index.html')
def login_page(request):
    if request.method=="POST":
        name=request.POST.get('username')
        password=request.POST.get('password')
        print(name,password)
        user=authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            ids = Register.objects.values_list('typ', flat=True).filter(name=name)
            if 'farmer' in ids:
                return HttpResponse("<h1>Login successfully!</h1><br><a style='color: green;' href='/farmerpage'><button>Return to Dashboard</button></a>")
            else :
                return HttpResponse("<h1>Login successfully!</h1><br><a style='color: green;' href='/consumerpage'><button>Return to Dashboard</button></a>")
        else:
            return HttpResponse("check username and password")
    return render(request,'Home/login.html')

def contact(request):
    if request.method=="POST":
        print(request)
        # name = request.POST.get('name', '')
        # email = request.POST.get('email', '')
        # phone = request.POST.get('phone', '')
        # desc = request.POST.get('desc', '')
        # contact = Contact(name=name, email=email, phone=phone, desc=desc)
        # contact.save()
    return render(request, 'Home/contact.html')
