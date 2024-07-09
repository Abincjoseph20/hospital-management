from django.shortcuts import render
from .models import Departments
# Create your views here.
def home(request):
    return render(request,'jmphospitals/home.html')

def about(request):
    return render(request,'jmphospitals/about.html')


def booking(request):
    return render(request,'jmphospitals/booking.html')


def doctors(request):
    return render(request,'jmphospitals/doctors.html')


def department(request):

    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'jmphospitals/department.html',dict_dept)


def contactus(request):
    return render(request,'jmphospitals/contactus.html')

def base(request):
    return render(request,'jmphospitals/base.html')