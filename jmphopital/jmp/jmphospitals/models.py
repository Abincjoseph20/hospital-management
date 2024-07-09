from django.db import models

# Create your models here.

class Departments(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()


class Doctors(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.CharField(max_length=200)
    dep_name=models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')