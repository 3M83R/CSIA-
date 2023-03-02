from curses import meta
from .models import Customers, hostels, OnDemand, reservations
from django import forms
from datetime import date, timedelta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime



today1 = date.today()
today2 = today1 + timedelta(weeks=157)


class Addhostels(forms.ModelForm):
    class Meta:
        model = hostels
        fields = ['name', 'checkindate', 'checkoutdate', 'address', 'adults', 'children', 'descriptions', 'distance', 'image', 'price_per_night']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class' : "form-control",
                    'placeholder' : "Hostel's Name",
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class' : "form-control",
                    'placeholder' : "Hostel's Address",
                }
            ),
            'checkindate': forms.DateInput(
                attrs={
                    'class' : "form-control",
                    'type': 'date',
                    'min': today1,
                    'value': today1
                }
            ),
            'checkoutdate': forms.DateInput(
                attrs={
                    'class' : "form-control",
                    'type': 'date',
                    'min': today2,
                    'value': today2
                }
            ),
            'adults': forms.NumberInput(
                attrs={
                    'class' : "form-control",
                    
                    }
                ),
            'children': forms.NumberInput(
                attrs={
                    'class' : "form-control",
                    }
                ),
            'description': forms.CharField(widget=forms.Textarea(
                attrs={
                    'type': 'text',
                    'class' : "form-control",
                    'placeholder' : "Description",
                }
            ),
        ),
        'distance': forms.NumberInput(
                attrs={
                    'class' : "form-control",
                    'placeholder' : "Distance from the center",
                }
            ),
        'image': forms.FileInput(
                attrs={
                    'class' : "form-control",
                    'placeholder' : "Image",
                    'multiple' : True,
                    'id' : "image",
                    'name' : "files",
                }
            ),
        'price_per_night': forms.NumberInput(
                attrs={
                    'class' : "form-control",
                    'placeholder' : "The price for one night",
                }
            ),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['first_name', 'email', 'message']
        widgets = {
            'message' : forms.Textarea( 
                attrs={
                    'rows': "5",
                    'class': "w3-input w3-padding-16 w3-border"
                }
            ),
            'first_name' : forms.TextInput( 
                attrs={
                    'class': "w3-input w3-padding-16 w3-border"
                }
            ),
            'email' : forms.EmailInput( 
                attrs={
                    'class': "w3-input w3-padding-16 w3-border"
                }
            )
        }


class OnDemandForm(forms.ModelForm):
    class Meta:
        model = OnDemand
        fields = ['first_name', 'email', 'guide', 'guide_tours', 'car_rental']
        widgets = {
            'guide' : forms.CheckboxInput( 
                attrs={
                    'class' : "form-check-input mt-0"
                }
            ),
            'guide_tours' : forms.CheckboxInput( 
                attrs={
                    'class' : "form-check-input mt-0"
                }
            ),
            'car_rental' : forms.CheckboxInput( 
                attrs={
                    'class' : "form-check-input mt-0"
                }
            ),
            'first_name' : forms.TextInput( 
                attrs={
                    'class' : "form-control",
                    'placeholder' : "Your first name",
                }
            ),
            'email' : forms.EmailInput( 
                attrs={
                    'class' : "form-control",
                    'placeholder' : "Your email",
                }
            )
        }

class ReservationForm(ModelForm):
    class Meta:
        model = reservations
        fields = ['hostel', 'checkindate', 'checkoutdate']



