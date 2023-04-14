
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
        pimg=request.POST.get('pimg','')
        fimg=request.POST.get('fimg','')
        cimg=request.POST.get('cimg','')
        my_user=User.objects.create_user(name,email,password)
        my_user.save()
        reg =Register(name=name,email=email,adress=adress,phone=phone,pinCode=pinCode,password=password,pimg=pimg,cimg=cimg,fimg=fimg,typ='farmer')
        reg.save()
    return render(request,'farmregister/farmregister1.html')
