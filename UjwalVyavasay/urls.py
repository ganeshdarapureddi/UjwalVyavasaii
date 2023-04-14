"""UjwalVyavasay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path( 'Farmers/f_account/',include('Farmers.f_account.urls')),
    path( 'Farmers/f_upload/',include('Farmers.f_upload.urls')),
    path( 'Consumers/c_account/',include('Consumers.c_account.urls')),
    path('farmorder/', include('Farmers.farmorder.urls')),
    path('farmregister/', include('Farmers.farmregister.urls')),
    path('login/farmregister/', include('Farmers.farmregister.urls')),
    path('consregister/', include('Consumers.consregister.urls')),
    path('consumerpage/', include('Consumers.consumerpage.urls')),
    path('farmerpage/', include('Farmers.farmerpage.urls')),
    path('consorder/', include('Consumers.consorder.urls')),
    path('',include('Home.urls')),
    path('login/farmregister/home/',include('Home.urls')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
