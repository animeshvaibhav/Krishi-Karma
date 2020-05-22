from django.urls import path
from . import views
#from .models import State,Crop,District,Farmer,Category,Soil


urlpatterns = [
    path('', views.index, name='index'),
    path('apply/', views.apply, name='apply'),
    path('farmer/', views.farmer, name='farmer',),
    path('detail/<farmerId>', views.detail, name ='detail'),
    path('dietician/', views.dietician, name='dietician'),
    path('donate/', views.donate, name='donate'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('ajax/update_district/', views.update_district, name='update_district'),
    path('ajax/update_crop/', views.update_crop, name='update_crop'),
    
]