from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_page),
    path('home/',views.home_page),
<<<<<<< Updated upstream
    path('login/',views.login_page,name='login'),
    path('contact/',views.contact)
=======
    path('login/',views.login_page),
    path('contact/',views.contact),
    
>>>>>>> Stashed changes
]
