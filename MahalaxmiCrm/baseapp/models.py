from datetime import datetime
import email
from statistics import mode
from django.db import models
from django.forms import CharField
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

class Agreement(models.Model):
    client_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    phone_no = PhoneNumberField(null=False, blank=False, unique=True)
    property_name = models.CharField(max_length=200, default='My Property')
    project_name = models.CharField(max_length= 200, default='My Project')
    payment_status = models.CharField(max_length=200, choices=(("Paid","Paid"), ("Unpaid","Unpaid"),("Party Paid","Party Paid")))
    agreement_id = models.CharField(max_length=200)
    agreement_date =  models.DateField()

class Project(models.Model):
    sr_no = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=400)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    project_description = models.CharField(max_length=1000)
    project_area = models.IntegerField(default=0)

#MASTERS 

class Source(models.Model):
    source_name = models.CharField(max_length=200)

class Property_Type(models.Model):
    properties = models.CharField(max_length=200, choices = (("Residential","Residential"), ("Flat", "Flat"), ("Commercial", "Commercial"), ("Bunglow","Bunglow")))
    sub_property = models.CharField(max_length=200, default="Company")

class Amenities(models.Model):
    amenity = models.CharField(max_length= 200)

#ADMIN

class Add_Telecaller(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length = 200, unique=True)
    dob = models.DateField()
    qualification = models.CharField(max_length=200, choices = (("12thPass","12thPass"),("b.b.a","b.b.a"),("b.s.c","b.s.c"),("M.B.A","M.B.A"),("B.COM","B.COM")))
    experience = models.IntegerField(default = 0)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length= 200)
    pin = models.IntegerField(default=0)

class Add_SalesPerson(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length = 200, unique=True)
    dob = models.DateField()
    qualification = models.CharField(max_length=200, choices = (("12thPass","12thPass"),("b.b.a","b.b.a"),("b.s.c","b.s.c"),("M.B.A","M.B.A"),("B.COM","B.COM")))
    experience = models.IntegerField(default = 0)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length= 200)
    pin = models.IntegerField(default=0)

class Add_Sites(models.Model):
    site_name = models.CharField(max_length=200)
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    property_type = models.CharField(max_length=200, choices = (("Villa","Villa"),("1 BHK","1 BHK"),("2 BHK","2 BHK"),("3 BHK","3 BHK"),("Office","Office")))
    location = models.CharField(max_length=500)

#Telecaller

class NewLead_Telecaller(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length = 200, unique=True)
    dob = models.DateField()
    interested_property = models.CharField(max_length=200, choices = (("Villa","Villa"),("1 BHK","1 BHK"),("2 BHK","2 BHK"),("3 BHK","3 BHK"),("Commercial","Commercial")))
    budget = models.IntegerField(default = 0)
    next_followup = models.DateField()


class FollowUps_Telecaller(models.Model):
    name = models.CharField(max_length= 200)
    phone_no = models.CharField(max_length = 200, unique=True)
    followUp_By = models.CharField(max_length = 200)
    followUp_date = models.DateField()
    remarks = models.CharField(max_length=300)

class Visit_Telecaller(models.Model):
    employee_name = models.CharField(max_length = 200)
    site_details = models.CharField(max_length = 500)
    visit_date = models.DateField()
    remarks = models.CharField(max_length=300)

#SalesPerson

class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length = 200, unique=True)
    project_type = models.CharField(max_length=300)
    property_type = models.CharField(max_length=200, choices = (("Villa","Villa"),("1 BHK","1 BHK"),("2 BHK","2 BHK"),("3 BHK","3 BHK"),("Commercial","Commercial")))
    salesperson = models.CharField(max_length=300)
    amount = models.CharField(max_length=300)

