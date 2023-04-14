from django.shortcuts import render
from django.http import HttpResponse
from  Home.models import Order
from  Home.models import Upload

def funroute3(request):   
    name = request.user
    upload = Upload.objects.all()
    length = len(upload)
    sum=0
    sumor=0
    flagup=0
    flagor=1
    for i in upload:
        sum += i.price
    if( sum==0 ):
        flagup=1
    params = {'order': upload, 'length':length, 'name':name, 'total':sum,'flagup':flagup,'flagor':flagor,'sumor':sumor}
    return render(request,'farmorder/farmorder1.html',params)