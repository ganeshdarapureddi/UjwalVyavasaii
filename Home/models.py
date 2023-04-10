from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Register( models.Model ):
    Name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    adress = models.CharField(max_length=20)
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator('^[0-9]{10}$', ('country code is not required'))],
        primary_key=True)
    pinCode = models.CharField(
        max_length=6,
        validators=[RegexValidator('^[0-9]{6}$',('Invalid postal code'))])
    password = models.CharField(max_length=30)

class Upload(models.Model):
    pName=models.CharField(max_length=20)
    price=models.FloatField(max_length=5)
    maxQty=models.FloatField(max_length=5)
    dTime=models.DateTimeField()
    phone=models.ForeignKey(Register,on_delete=models.CASCADE)
    PImage = models.ImageField(default="default.jpg", upload_to="profile_pics")

class Orders(models.Model):
    phone=models.ForeignKey(Register,on_delete=models.CASCADE,related_name='+')
    quant=models.FloatField(max_length=5)
    sPrc=models.FloatField(max_length=5)
    aTime=models.DateTimeField()
    pName=models.ForeignKey(Upload,on_delete=models.CASCADE,related_name='pName+')
    pImage=models.ForeignKey(Upload,on_delete=models.CASCADE,related_name='pImage+')


    