from django.contrib import admin
from .models import Register,Upload,Order,Contact
# Register your models here.
admin.site.register(Register)
admin.site.register(Upload)
admin.site.register(Order)
admin.site.register(Contact)