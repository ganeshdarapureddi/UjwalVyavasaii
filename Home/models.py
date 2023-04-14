from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Register( models.Model ):
    name = models.CharField(max_length=30,default="")
    email = models.EmailField(max_length=40,default="")
    adress = models.CharField(max_length=50,default="")
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator('^[0-9]{10}$', ('country code is not required'))],
        primary_key=True,default="")
    pinCode = models.CharField(
        max_length=6,
        validators=[RegexValidator('^[0-9]{6}$',('Invalid postal code'))],default="")
    password = models.CharField(max_length=30,default="")
    cpassword = models.CharField(max_length=30,default="")
    pimg = models.ImageField(default="", upload_to='shop/uploads')
    fimg = models.ImageField(default="", upload_to='shop/uploads')
    cimg = models.ImageField(default="", upload_to='shop/uploads')

    def __str__(self):
        return self.name

class Upload(models.Model):
    pName=models.CharField(max_length=30,default="")
    price=models.FloatField(max_length=10,default="")
    maxQty=models.FloatField(max_length=10,default="")
    dTime=models.DateField(default="")
    phone=models.ForeignKey(Register,on_delete=models.CASCADE,default="",related_name='phone+')
    PImage = models.ImageField(default="", upload_to='shop/uploads')

    def __str__(self):
        return self.pName

class Order(models.Model):
    id =  models.BigAutoField(primary_key=True)
    phone=models.ForeignKey(Register,on_delete=models.CASCADE,related_name='+',default="")
    quant=models.FloatField(max_length=10,default="")
    sPrc=models.FloatField(max_length=10,default="")
    aTime=models.DateField(default="")
    pName=models.ForeignKey(Upload,on_delete=models.CASCADE,related_name='pName+',default="")
    pImage=models.ForeignKey(Upload,on_delete=models.CASCADE,related_name='pImage+',default="") #,upload_to='shop/orders'
    dTime=models.ForeignKey(Upload,on_delete=models.CASCADE,related_name='dTime+',default="")

    def __str__(self):
         return str(self.id)
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name    