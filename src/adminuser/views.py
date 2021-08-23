from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request,"adminuserhome.html",{"adminuser":"hello admin"})

def registerdoctor(request):
    return render(request,"adminregisterdoctor.html")

def registerpatient(request):
    return render(request,"adminregisterpatient.html")

def adddoctor(request):
    return render(request,"viewdoctor.html")

def addpatient(request):
    return render(request,"viewpatient.html")