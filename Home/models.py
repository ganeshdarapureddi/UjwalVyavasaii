from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Register( models.Model ):
    Name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    adress = models.CharField(max_length=20)
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator('^[0-9]{10}$', ('country code is not required'))])
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
    P_image = models.ImageField(default="default.jpg", upload_to="profile_pics")

class Orders(models.Model):
    mobile=models.ForeignKey(Register,on_delete=models.CASCADE,related_name='phone')
    quant=models.FloatField(max_length=5)
    s_prc=models.FloatField(max_length=5)
    a_time=models.DateTimeField()
    P_Name=models.ForeignKey(Upload,on_delete=models.CASCADE,related_name='P_Name')
    P_image=models.ForeignKey(Upload,on_delete=models.CASCADE,related_name='P_image')


    