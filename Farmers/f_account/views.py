from django.shortcuts import render
from Home.models import Register
# Create your views here.
def f_account(request):
    name = request.user
    account = Register.objects.filter(name=name)
    acc = Register.objects.get(name=name)
    existpass = Register.objects.values_list('password',flat=True).filter(name=name)
    params = { 'account':account }   
    if request.method=="POST":      
        adress = request.POST.get('adress')
        pincode = request.POST.get('pincode')
        oldpass = request.POST.get('oldpass')
        new1pass = request.POST.get('new1pass')
        acc.adress = adress
        acc.pinCode = pincode
        acc.save()
        if( existpass==oldpass ):
            acc.password = new1pass
            acc.save()
    return render(request,'f_account/f_account.html',params)