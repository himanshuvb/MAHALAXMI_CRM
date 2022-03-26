from datetime import datetime
from statistics import mode
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_no = PhoneNumberField(null=False, blank=False, unique=True)
    DOB = models.DateField()
    PAN = models.CharField(max_length=10)
    source = models.CharField(max_length=100)

class Agent(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_no = PhoneNumberField(null=False, blank=False, unique=True)
    DOB = models.DateField()
    PAN = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField(default=0)
    
class Properties(models.Model):
    property_title = models.CharField(max_length=200)
    select_project = models.CharField(max_length=100, choices=(("Project 1","Project 1"), ("Project 2","Project 2"),("Project 3","Project 3")))
    select_property_type = models.CharField(max_length=50, choices=(("Resendintial","Resendintial"), ("Commercial","Commercial"), ("Other","Other")))
    size = models.IntegerField(default=0)
    property_age = models.IntegerField(default=0)
    reference = models.CharField(max_length=100)
    agent_contact = PhoneNumberField(null=False, blank=False, unique=True)
    cost_of_property = MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=100)
    # amenities = 
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    property_description = models.CharField(max_length=500)

class Payment(models.Model):
    sr_no = models.AutoField(primary_key=True)
    phone_no = PhoneNumberField(null=False, blank=False)
    email = models.EmailField(max_length=254)
    client_name = models.CharField(max_length=200)
    property_name = models.CharField(max_length=200)
    proj_name = models.CharField(max_length=200)
    pay_id = models.CharField(max_length=200)
    pay_date = models.DateField()
    property_description = models.CharField(max_length=500)
