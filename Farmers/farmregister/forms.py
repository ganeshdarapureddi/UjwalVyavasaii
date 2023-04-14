from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField 
from django.forms.forms import Form  
  
class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='name', min_length=5, max_length=150)  
    email = forms.EmailField(label='Email')  
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput)  
    cpassword = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)  
  
    def username_clean(self):  
        name = self.cleaned_data['name'].lower()  
        new = User.objects.filter(name = name)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return name  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password = self.cleaned_data['password']  
        cpassword = self.cleaned_data['cpassword']  
  
        if password and password and cpassword!= cpassword:  
            raise ValidationError("Password don't match")  
        return cpassword  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['name'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password']  
        )  
        return user  