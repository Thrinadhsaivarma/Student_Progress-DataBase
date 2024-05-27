from django.db import models

# Create your models here.
class Student(models.Model):
    roll_number=models.CharField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    marks=models.CharField(max_length=100,unique=True)
    home_address=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=10)
