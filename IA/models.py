import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.conf import settings

class hostels(models.Model):
    name = models.CharField('Hostels name', max_length=120)
    checkindate = models.DateField(blank=True, null=True)
    checkoutdate = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=300)
    adults = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(6)])
    children = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(6)])
    descriptions = models.TextField(blank=True)
    customers = models.ManyToManyField('reservations', blank=True)
    image = models.ImageField(blank=True, null=True, upload_to = 'images/')
    distance = models.DecimalField(null=True, blank=True, validators=[MinValueValidator(0)], max_digits=5, decimal_places=2)  
    ratings = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, validators=[MinValueValidator(0)])
    price_per_night = models.DecimalField(blank=True, max_digits=8, decimal_places=2, null=True, validators=[MinValueValidator(0.00)])

    def __str__(self):
        return self.name

class admin(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    
    def __str__(self):
        return self.username

class reservations(models.Model):
    surname = models.CharField('Surname', max_length=30)
    phone_no = models.CharField('Phone Number', max_length=12)
    email = models.EmailField('Email Address')
    hostel = models.ForeignKey(hostels, on_delete=models.CASCADE, null=True, blank=True)
    cancel = models.BooleanField(default=False)
    checkindate = models.DateField(blank=True, null=True)
    checkoutdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.surname

class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

class OnDemand(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    guide = models.BooleanField(blank = True)
    guide_tours = models.BooleanField(blank = True)
    car_rental = models.BooleanField(blank = True)
