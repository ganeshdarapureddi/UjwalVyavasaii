from django.shortcuts import render

def home_page(request):
    return render(request,'Home/index.html')
def login_page(request):
    return render(request,'Home/login.html')
