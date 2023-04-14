from django.shortcuts import render
from django.http import HttpResponse
from  Home.models import Order

def funroute3(request):   
    name = request.user
    orders = Order.objects.all()
    length = len(orders)
    sum=0
    flag=0
    for i in orders:
        sum += i.sPrc
    if( sum==0 ):
        flag=1
    params = {'order': orders, 'length':length, 'name':name, 'total':sum,'flag':flag}
    return render(request,'consorder/consorder1.html',params)