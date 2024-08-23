from django import forms
from .models import Booking
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
class DateInput(forms.DateInput): #for date and time purpus
    input_type = 'date'


class BookingForms(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['p_name','p_phone','p_email','doc_name','booking_date']

        #for form styling purpus it is a dictonory
        widgets = {
            'p_name': forms.TextInput(attrs={'class':'form-control'}),
            'p_phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'p_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'doc_name': forms.Select(attrs={'class': 'form-control'}),
            'booking_date': DateInput(),
        }


        labels ={
            'p_name':'Patient Name',
            'p_phone':'Patient Phone',
            'p_email': 'Patient Email',
            'doc_name': 'Doctor Name',
            'booking_date':'Booking Date'
        }


class PatientRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):  #https://youtu.be/qwFBXuEeg1U?si=iqv_jC1TUZ6Kdm1k 2:33:33
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

