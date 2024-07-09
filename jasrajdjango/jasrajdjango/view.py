from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def Home(request):
    return render(request, 'Home.html')

def AboutUs(request):
    return render(request, 'About Us.html')

def ContactUs(request):
    return render(request, 'Contact Us.html')

def Qualitative(request):
    return render(request, 'Qualitative.html')

def Quantitative(request):
    return render(request, 'Quantitative.html')

def OtherService(request):
    return render(request, 'Other Service.html')

def Industry(request):
    return render(request, 'Industry.html')

def Coverage(request):
    return render(request, 'Coverage.html')

def JionOurPanel(request):
    return render(request, 'Jion Our Panel.html')