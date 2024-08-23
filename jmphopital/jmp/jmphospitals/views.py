from django.shortcuts import render,redirect
from .models import Departments,Doctors
from .forms import BookingForms,PatientRegistrationForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'jmphospitals/home.html')

def about(request):
    return render(request,'jmphospitals/about.html')


def booking(request):
    if request.method == 'POST':
        form = BookingForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'jmphospitals/conform.html')
    form = BookingForms()
    dict_form = {
        'form':form
    }
    return render(request,'jmphospitals/booking.html',dict_form)


class PatientsRegistration(View):
    def get(self,request):
        form = PatientRegistrationForm()
        return render(request,'jmphospitals/Registration.html',locals())
    def post(self,request):
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"congratulation User Registration Succesfull")
        else:
            messages.warning(request,'Invalid Input Data')
        return render(request, 'jmphospitals/Registration.html', locals())

def doctors(request):
    dict_doc = {
        'doctors':Doctors.objects.all()
    }
    return render(request,'jmphospitals/doctors.html',dict_doc)



def loggout(request):
    logout(request)
    return redirect('login')


def department(request):

    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'jmphospitals/department.html',dict_dept)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Construct the email message
        subject = f"New Contact Form Submission from {name}"
        message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        from_email = email  # or you can use DEFAULT_FROM_EMAIL
        recipient_list = ['ebincjoseph2@gmail.com']  # Replace with the recipient's email

        # Send the email
        send_mail(subject, message_body, from_email, recipient_list)

        # Optionally, add a success message or redirect
        return HttpResponse("Thank you for your message. We will get back to you soon.")

    return render(request, 'jmphospitals/contactus.html')


def base(request):
    return render(request,'jmphospitals/base.html')