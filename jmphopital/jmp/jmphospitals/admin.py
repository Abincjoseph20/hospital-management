from django.contrib import admin
from .models import Departments,Doctors,Booking

# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Booking)