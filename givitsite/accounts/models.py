from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    date_of_birth = models.DateField(max_length=8)
    address_street = models.CharField(max_length=100)
    address_home_number = models.IntegerField()
    address_city = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField()
    field_of_study = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    current_year = models.CharField(max_length=50)
    scholarship = models.CharField(max_length=100)
    type_of_friendship = models.CharField(max_length=100)


