from Home.models import Upload
from django.shortcuts import redirect, render  ,HttpResponse
from django.contrib import messages  

# Create your views here.
def f_upload(request):
    if request.method=="POST":
        name=request.POST.get('pname','')
        price=request.POST.get('price','')
        maxQty=request.POST.get('quantity','')
        time=request.POST.get('time','')
        pimg=request.POST.get('pimg','')
        print(name,price,maxQty)
        reg =Upload(pName=name,price=price,maxQty=maxQty,dTime=time,PImage=pimg)
        reg.save()
        return render(request, './farmerpage/farmerpage.html')
    return render(request,'f_upload/upload.html')