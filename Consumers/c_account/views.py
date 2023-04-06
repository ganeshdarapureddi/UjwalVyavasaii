from django.shortcuts import render

# Create your views here.
def account(request):
    return render(request,'c_account/c_account.html')