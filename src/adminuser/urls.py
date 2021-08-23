from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome,name="welcome"),
    path('registerdoctor',views.registerdoctor,name="registerdoctor"),
    path('registerpatient',views.registerdoctor,name="registerpatient"),
    path('adddoctor',views.adddoctor,name="adddoctor"),
    path('addpatient',views.addpatient,name="addpatient")
]