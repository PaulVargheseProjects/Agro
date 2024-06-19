from django.db import models
from officer.models import Seminar
from accounts.models import User, Lab

# Create your models here.

class SeminarBooking(models.Model):
    sem_book_id = models.BigAutoField(primary_key=True)
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.seminar.name

class Test(models.Model):
    test_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class LabType(models.Model):
    lab_type_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Test(models.Model):
    test_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lab_type = models.ForeignKey(LabType, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class LabAppointment(models.Model):
    lab_book_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, default=None)
    booked_date = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username


class Land(models.Model):
    land_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='land')
    location = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=6, default=None, null=True, blank=True)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class LandBooking(models.Model):
    land_book_id = models.BigAutoField(primary_key=True)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.land.name


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Cereals/Grains', 'Cereals/Grains'),
        ('Fruits', 'Fruits'),
        ('Vegetables', 'Vegetables')
    )
    product_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ProductBooking(models.Model):
    pro_book_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    booked_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.product.name

class Cart(models.Model):
    cart_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    booked_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.product.name


class UserQuery(models.Model):
    TO = (
        (1, 'To Officer'),
        (2, 'To Lab'),
    )
    query_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    to = models.IntegerField(choices=TO)
    reply = models.TextField(default='', blank=True)
    def __str__(self):
        return self.query