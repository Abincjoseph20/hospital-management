from django import forms
from .models import Booking

class DateInput(forms.DateInput): #for date and time purpus
    input_type = 'date'


class BookingForms(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        #for form styling purpus it is a dictonory
        widgets = {
            'p_name': forms.TextInput(attrs={'class':'form-control'}),
            'p_phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'p_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'doc_name': forms.Select(attrs={'class': 'form-control'}),
            'booking_date': DateInput(),
        }
