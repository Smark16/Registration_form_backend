from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAccounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    
    def __str__(self):
        return f"{self.user.username}"

class PersonalInfomation(models.Model):
    Admission_No = models.CharField(max_length=100)
    Surname = models.CharField(max_length=64)
    Other_Names = models.CharField(max_length=64)
    sex_choices = (('Female', 'Female'), ('Male', 'Male'))
    Sex = models.CharField(max_length=10, default='Choose Gender')
    Date_Of_Birth = models.DateField()
    Age = models.PositiveIntegerField()
    Postal_Address = models.CharField(max_length=64, null=True, blank=True)
    Telephone = models.PositiveBigIntegerField()
    Email = models.EmailField(max_length=100)
    Home_District = models.CharField(max_length=100)
    Subcounty = models.CharField(max_length=100)
    Nationality = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=100)
    Present_Job_TiTle = models.CharField(max_length=100)


class Employer(models.Model):
    Employer = models.CharField(max_length=100)
    Postal_Address = models.CharField(max_length=100)
    Telephone = models.PositiveBigIntegerField()
    Email = models.EmailField(max_length=100)
    
