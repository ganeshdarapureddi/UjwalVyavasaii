from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Register( models.Model ):
    Name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    adress = models.CharField(max_length=20)
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator('^[0-9]{10}$', ('country code is not required'))],primary_key=True)
    pinCode = models.CharField(
        max_length=6,
        validators=[RegexValidator('^[0-9]{6}$',('Invalid postal code'))])
    password = models.CharField(max_length=30)

class Upload(models.Model):
    P_Name=models.CharField(max_length=20)
    price=models.FloatField(max_length=5)
    max_qty=models.FloatField(max_length=5)
    d_time=models.DateTimeField()
    phone=models.ForeignKey(Register,on_delete=models.CASCADE)
    P_image = models.ImageField(default="default.jpg")

class Orders(models.Model):
    mobile=models.ForeignKey(Register,on_delete=models.CASCADE)
    a_time=models.DateTimeField()
    
    