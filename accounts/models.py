from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

# Create your models here.


def phone_validator(value):
    if value.isdigit() and len(value) == 10:
        return value
    else:
        raise ValidationError('Phone number must be of 10 digits')

def aadhar_validator(value):
    if value.isdigit() and len(value) == 12:
        return value
    else:
        raise ValidationError('Aadhar number must be of 12 digits')

class User(AbstractUser):
    user_id = models.BigAutoField(primary_key=True)
    phone = models.CharField(max_length=10, validators=[phone_validator], unique=True)
    aadhar = models.ImageField(upload_to='aadhar')
    address = models.TextField(max_length=100)
    user_type = models.CharField(max_length=10, default='officer')
    password = models.CharField(max_length=100, validators=[validate_password])
    def __str__(self):
        return self.username

class Lab(models.Model):
    lab_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10, validators=[phone_validator], unique=True)
    registration_number = models.CharField(max_length=10)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name




