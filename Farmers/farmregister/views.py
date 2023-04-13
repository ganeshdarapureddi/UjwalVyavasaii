
from Home.models import Register
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm  
from .forms import CustomUserCreationForm  

def funroute3(request):
    if request.method=="POST":
        form = UserCreationForm()  
        if form.is_valid():  
            form.save()
        else:  
            form = UserCreationForm()  
            context = { 'form':form  }
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        adress=request.POST.get('adress','')
        phone=request.POST.get('phone','')
        pinCode=request.POST.get('pinCode','')
        password=request.POST.get('password','')
        cpassword =request.POST.get('cpassword ','')
        pimg=request.POST.get('pimg','')
        fimg=request.POST.get('fimg','')
        cimg=request.POST.get('cimg','')
        reg =Register(name=name,email=email,adress=adress,phone=phone,pinCode=pinCode,password=password,cpassword=cpassword,pimg=pimg,cimg=cimg,fimg=fimg)
        reg.save()
    return render(request,'farmregister/farmregister1.html',context)
    
