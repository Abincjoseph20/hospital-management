from django.urls import path,include
from .import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('department/', views.department, name='departments'),
    path('contactus/', views.contactus, name='contact'),
    path('base/', views.base, name='base'),
]