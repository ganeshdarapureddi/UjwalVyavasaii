
from Home.models import Register
from django.contrib.auth.models import User
from django.shortcuts import redirect, render  ,HttpResponse
from django.contrib import messages  

def funroute3(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        adress=request.POST.get('adress','')
        phone=request.POST.get('phone','')
        pinCode=request.POST.get('pinCode','')
        password=request.POST.get('password','')
        cpassword=request.POST.get('cpassword','')
        pimg=request.POST.get('pimg')
        if password==cpassword:
            my_user=User.objects.create_user(name,email,password)
            my_user.save()
            reg =Register(name=name,email=email,adress=adress,phone=phone,pinCode=pinCode,password=password,pimg=pimg,typ='customer')
            reg.save()
            return HttpResponse("<h1>Registered successfully! now login to your account</h1><br><a style='color: green;' href='/login'>return to login</a>")
        else:
            return HttpResponse("check password and confirm password")
    return render(request,'consregister/consregister11.html')
