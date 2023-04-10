from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Register( models.Model ):
    Name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    adress = models.CharField(max_length=20)
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator('^[0-9]{10}$', _('country code is not required'))])
    pinCode = models.CharField(
        max_length=6,
        validators=[RegexValidator('^[0-9]{6}$', _('Invalid postal code'))])
    password = models.CharField(max_length=30)
    