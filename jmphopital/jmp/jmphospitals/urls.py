from django.urls import path
from .import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('department/', views.department, name='departments'),
    path('contactus/', views.contact, name='contact'),
    path('base/', views.base, name='base'),
    path('registrations', views.PatientsRegistration.as_view(), name="registration"),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='jmphospitals/login.html',authentication_form=LoginForm),name='login'),
    path('logout/', views.loggout, name='logout'),
]

#(.venv) PS E:\abin\jmp\jmphopital\jmp> python manage.py runserver (path)