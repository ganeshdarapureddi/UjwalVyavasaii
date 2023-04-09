from django.shortcuts import render
from django.http import HttpResponse


def funroute3(request):
    return render(request,'farmerpage/farmerpage.html')