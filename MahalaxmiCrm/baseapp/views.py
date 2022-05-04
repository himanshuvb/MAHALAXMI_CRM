import contextvars
import email
from http import client
import re
from xml.dom.xmlbuilder import DOMBuilder
from django.contrib.auth import authenticate, login, logout
from .models import Add_Telecaller, Agreement, Amenities, Booking, Client,Agent, FollowUps_Telecaller,Payment,Properties, Property_Type, Source,Project, Add_SalesPerson, NewLead_Telecaller, Add_Sites, Visit_Telecaller
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files import File
import phonenumbers as pn 

# Create your views here.
def user_login(request):
    if request.method == "GET":
        return render(request,'baseapp/page-login.html')
    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('dashboard_admin') 
                else:
                    return render(request, "baseapp/page-login.html", context={"error": "User is not active"})
            else:
                return render(request, "baseapp/page-login.html", context={"error": "Login credentials are incorrect"})


def dashboard(request):    
    return render(request,'baseapp/dashboard.html')

def supports(request):
    return render(request,'baseapp/supports.html')

def home(request):
    return render(request, 'baseapp/index3.html')

def add_client(request):
    if(request.method =="GET"):
        return render(request, 'baseapp/clients/add-client.html')
    if(request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone']
        DOB = request.POST['dob']
        PAN = request.POST['pan']
        Source = request.POST['source']
        
        client = Client(name = name,email = email,phone_no=phone_no,DOB=DOB,PAN=PAN,source=Source)
        client.save()
        #pan number must be unique it is not for now 
        return redirect('dashboard')


def list_clients(request):
    client_list = Client.objects.all()
    return render(request, 'baseapp/clients/list-clients.html',context={"all_client": client_list})

def add_agent(request):
    if (request.method=="GET"):
        return render(request, 'baseapp/agents/add-agent.html')
    if(request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone']
        DOB = request.POST['dob']
        PAN = request.POST['pan']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pin']
        
        agent = Agent(name = name,email = email,phone_no=phone_no,DOB=DOB,PAN=PAN,city=city,state=state,pincode=pincode)
        agent.save()
        #pan number must be unique it is not for now 
        return redirect('dashboard')


def list_agents(request):
    agent_list = Agent.objects.all()
    return render(request, 'baseapp/agents/list-agents.html',context={"all_agent": agent_list})

def add_project(request):
    if (request.method=="GET"):
        return render(request, 'baseapp/projects/add_project.html')
    if(request.method=="POST"):
        project_name = request.POST['project_name']
        location = request.POST['location']
        image =File(request.FILES.get('image'))
        project_description = request.POST['project_description']
        project_area = request.POST['project_area']

        project = Project(
        project_name = project_name,
        location = location,
        image = image,
        project_description = project_description,
        project_area = project_area

        )

        project.save()
        return redirect('dashboard')

def view_project(request):
     project_list = Project.objects.all()
     return render(request, 'baseapp/projects/view_project.html',context={'projects':project_list})
def add_properties(request):
    if (request.method=="GET"):
        return render(request, 'baseapp/properties/add-properties.html')
    if(request.method=="POST"):
        property_title = request.POST['property_title']
        select_project = request.POST['select_project']
        select_property_type = request.POST['select_property_type']
        size = request.POST['size']
        property_age = request.POST['property_age']
        reference = request.POST['reference']
        agent_contact = request.POST['agent_contact']
        cost_of_property = request.POST['cost_of_property']
        img = File(request.FILES.get('img'))
        property_description = request.POST['property_description']        

        properties = Properties(
            property_title=property_title, 
            select_project=select_project, 
            select_property_type=select_property_type, 
            size=size, property_age=property_age, 
            reference=reference, 
            agent_contact=agent_contact, 
            cost_of_property=cost_of_property,
            img=img,
            property_description=property_description
        )
        properties.save()
        return redirect('dashboard')

def list_properties(request):
    properties_list = Properties.objects.all()
    return render(request, 'baseapp/properties/list-properties.html',context={"all_properties": properties_list})

def all_leads(request):
    return render(request, 'baseapp/leads/Allleads.html')

def fresh_leads(request):
    return render(request, 'baseapp/leads/Fresh.html')

def old_followups(request):
    return render(request, 'baseapp/leads/Old.html')

def todays_followups(request):
    return render(request, 'baseapp/leads/Todays.html')

def upcoming_followups(request):
    return render(request, 'baseapp/leads/UpComing.html')

def add_new_leads(request):
    return render(request, 'baseapp/leads/AddNewLeads.html')

def add_user(request):
    return render(request, 'baseapp/settings/adduser.html')

def history(request):
    return render(request, 'baseapp/settings/history.html')

def password(request):
    return render(request, 'baseapp/settings/password.html')

def masters_add_source(request):
    if request.method == "GET":
        sources= Source.objects.all()
        return render(request, 'baseapp/masters/master_add_source.html',context={"sources":sources}) 
    if request.method == "POST":
        source_name = request.POST['source_name']

        source = Source()
        source.source_name= source_name

        source.save()
        return redirect('masters_add_source')
        

   


def masters_add_amenities(request):
    if request.method == "GET":
        amenities= Amenities.objects.all()
        return render(request, 'baseapp/masters/master_addAmenities.html',context={"amenities":amenities}) 
    if request.method == "POST":
        amenity = request.POST['amenity']

        amenities = Amenities()
        amenities.amenity= amenity

        amenities.save()
        return redirect('masters_add_amenities')

def masters_add_property_type(request):

    if request.method == "GET":
        property_type= Property_Type.objects.all()
        return render(request, 'baseapp/masters/masters_addPropertyType.html',context={"property_type":property_type}) 
    if request.method == "POST":
        properties = request.POST['properties']
        sub_property = request.POST['sub_property']

        property_type = Property_Type()
        property_type.properties = properties
        property_type.sub_property = sub_property

        property_type.save()
        return redirect('masters_add_property_type')


def add_payment(request):
    if request.method=="GET":
        return render(request, 'baseapp/payments/add_payment.html')
    if request.method=="POST":
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        client_name = request.POST['client_name']
        property_name = request.POST['property_name']
        proj_name = request.POST['proj_name']
        pay_id = request.POST['pay_id']
        pay_date = request.POST['pay_date']

        new_pay = Payment()
        new_pay.phone_no = phone_no
        new_pay.email = email
        new_pay.client_name = client_name
        new_pay.property_name = property_name
        new_pay.proj_name = proj_name
        new_pay.pay_id = pay_id
        new_pay.pay_date = pay_date
        new_pay.save()

        return redirect('dashboard')

def delete_client(request,client_id):  
    
    client = get_object_or_404(Client,id=client_id)
    client.delete()
    return redirect("list_clients")



def view_payment(request):
    payment_list = Payment.objects.all()
    return render(request, 'baseapp/payments/view_payment.html',context={"payments":payment_list})

def add_agreement(request):
    if (request.method=="GET"):
        return render(request, 'baseapp/agreements/add_agreement.html')
    if(request.method=="POST"):
        client_name = request.POST['client_name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        property_name = request.POST['property_name']
        project_name = request.POST['project_name']
        payment_status = request.POST['payment_status']
        agreement_id = request.POST['agreement_id']
        agreement_date = request.POST['agreement_date']
        
        agreement = Agreement()
        agreement.client_name = client_name
        agreement.email = email
        agreement.phone_no = phone_no
        agreement.property_name = property_name
        agreement.property_name = property_name
        agreement.payment_status = payment_status
        agreement.agreement_id = agreement_id
        agreement.agreement_date= agreement_date
        agreement.save()

        return redirect('dashboard')
        

def view_agreement(request):
    agreement_list = Agreement.objects.all()
    return render(request, 'baseapp/agreements/view_agreement.html',context={"agreements":agreement_list})

def navbar_admin(request):
    return render(request, 'baseapp/admin/navbar_admin.html')

def navbar_telecaller(request):
    return render(request, 'baseapp/telecaller/navbar_telecaller.html')

def navbar_salesPerson(request):
    return render(request, 'baseapp/salesperson/navbar_salesPerson.html')

#SalesPerson

def sales_login(request):
    if (request.method == "GET"):
        return render(request, 'baseapp/salesperson/sales_login.html')
    if (request.method == "POST"):
        return redirect('booking_salesPerson')


def dashboard_salesPerson(request):
    return render(request, 'baseapp/salesperson/dashboard_salesPerson.html')

def booking_salesPerson(request):
    if(request.method =="GET"):
        return render(request, 'baseapp/salesperson/Booking_salesPerson.html')
    if(request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        project_type = request.POST['project_type']
        property_type = request.POST['property_type']
        salesperson = request.POST['salesperson']
        amount = request.POST['amount']
        
        booking = Booking(name = name,email = email, phone = phone, project_type=project_type, property_type=property_type,salesperson= salesperson, amount=amount)
        booking.save()
        #pan number must be unique it is not for now 
        return redirect('TotalBookings_salesPerson')

def TotalBookings_salesPerson(request):
    total_bookings = Booking.objects.all()
    return render(request, 'baseapp/salesperson/TotalBookings_salesPerson.html',context={"total_bookings": total_bookings})

def TodaysVisit_salesPerson(request):
    visitList_tele = Visit_Telecaller.objects.all()
    return render(request, 'baseapp/salesperson/TodaysVisit_salesPerson.html',context={"visitList_telecaller": visitList_tele})

def delete_salesperson(request,add_salesperson_id):
    salesperson = get_object_or_404(Add_SalesPerson,id=add_salesperson_id)
    salesperson.delete()
    return redirect("list_salesperson")

#SalesPerson -- FollowUps

def FollowUps_salesPerson(request):
    followUps_telecaller = FollowUps_Telecaller.objects.all()
    return render(request, 'baseapp/salesperson/FollowUps/followUps_salesperson.html',context={"followUps_telecaller": followUps_telecaller})

def OldFollowUps_salesPerson(request):
    return render(request, 'baseapp/salesperson/FollowUps/Old.html')

def TodaysFollowUps_salesPerson(request):
    return render(request, 'baseapp/salesperson/FollowUps/Today.html')

def UpComingFollowUps_salesPerson(request):
    return render(request, 'baseapp/salesPerson/FollowUps/UpComing.html')

# Telecaller

def telecaller_login(request):
    if (request.method == "GET"):
        return render(request, 'baseapp/telecaller/telecaller_login.html')
    if (request.method == "POST"):
        return redirect('VisitList_telecaller')

def dashboard_telecaller(request):
    return render(request, 'baseapp/telecaller/dashboard_telecaller.html')

#Lead
def NewLead_telecaller(request):
    if(request.method =="GET"):
        return render(request, 'baseapp/telecaller/Leads/newLead_telecaller.html')
    if(request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        interested_property = request.POST['interested_property']
        budget = request.POST['budget']
        next_followup = request.POST['next_followup']
        
        newLead_telecaller = NewLead_Telecaller(name = name,email = email, phone = phone, dob=dob, interested_property=interested_property,budget= budget, next_followup=next_followup)
        newLead_telecaller.save()
        #pan number must be unique it is not for now 
        return redirect('ListLead_telecaller')

def ListLead_telecaller(request):
    listLead_telecaller = NewLead_Telecaller.objects.all()
    return render(request, 'baseapp/telecaller/Leads/listLead_telecaller.html',context={"ListLead_telecaller": listLead_telecaller})

def TotalBookings_telecaller(request):
    return render(request, 'baseapp/telecaller/TotalBookings_telecaller.html')
#Visits

def addVisit(request):
    if(request.method =="GET"):
        return render(request, 'baseapp/telecaller/Visit/addVisit.html')
    if(request.method=="POST"):
        employee_name = request.POST['employee_name']
        site_details = request.POST['site_details']
        visit_date = request.POST['visit_date']
        remarks = request.POST['remarks']
        
        add_Visit = Visit_Telecaller(employee_name = employee_name,site_details= site_details,visit_date= visit_date, remarks = remarks )
        add_Visit.save()
        #pan number must be unique it is not for now 
        return redirect('VisitList_telecaller')

def VisitList_telecaller(request):
    visitList_tele = Visit_Telecaller.objects.all()
    return render(request, 'baseapp/telecaller/Visit/visitList_telecaller.html',context={"visitList_telecaller": visitList_tele})

def BookingList_telecaller(request):
    return render(request, 'baseapp/telecaller/BookingList_telecaller.html')

def deadLead_telecaller(request):
    return render(request, 'baseapp/telecaller/deadLead_telecaller.html')

def delete_telecaller(request,add_telecaller_id):
    telecaller = get_object_or_404(Add_Telecaller,id=add_telecaller_id)
    telecaller.delete()
    return redirect("list_telecaller")
    

#Telecaller --FollowUps

def OldFollowUps_telecaller(request):
    return render(request, 'baseapp/telecaller/FollowUps/Olds.html')

def TodaysFollowUps_telecaller(request):
    return render(request, 'baseapp/telecaller/FollowUps/Todays.html')

def UpComingFollowUps_telecaller(request):
    return render(request, 'baseapp/telecaller/FollowUps/UpComings.html')

def addFollowUps(request):
    if(request.method =="GET"):
        return render(request, 'baseapp/telecaller/FollowUps/addFollowUps.html')
    if(request.method=="POST"):
        name = request.POST['name']
        phone_no = request.POST['phone_no']
        followUp_By = request.POST['followUp_By']
        followUp_date = request.POST['followUp_date']
        remarks = request.POST['remarks']
        
        
        addFollowUps = FollowUps_Telecaller(name = name, phone_no = phone_no,followUp_By = followUp_By, followUp_date = followUp_date ,remarks= remarks)
        addFollowUps.save()
        #pan number must be unique it is not for now 
        return redirect('followups_telecaller')

def followUps_telecaller(request):
    followUps_telecaller = FollowUps_Telecaller.objects.all()
    return render(request, 'baseapp/telecaller/FollowUps/FollowUps_telecaller.html',context={"followUps_telecaller": followUps_telecaller})

#Admin 

def dashboard_admin(request):
    return render(request, 'baseapp/admin/dashboard_admin.html')
    
def add_telecaller(request):
    if(request.method =="GET"):
        return render(request, 'baseapp/admin/add_telecaller.html')
    if(request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        qualification = request.POST['qualification']
        experience = request.POST['experience']
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        
        add_telecaller = Add_Telecaller(name = name,email = email, phone = phone, dob=dob, qualification=qualification,experience= experience, city=city, state=state, pin= pin)
        add_telecaller.save()
        #pan number must be unique it is not for now 
        return redirect('list_telecaller')

def list_telecaller(request):
    list_telecaller = Add_Telecaller.objects.all()
    return render(request, 'baseapp/admin/list_telecaller.html',context={"all_telecaller": list_telecaller})

def add_salesperson(request):
    if(request.method =="GET"):
        return render(request, 'baseapp/admin/add_salesperson.html')
    if(request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        qualification = request.POST['qualification']
        experience = request.POST['experience']
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        
        add_salesperson = Add_SalesPerson(name = name,email = email, phone = phone, dob=dob, qualification=qualification,experience= experience, city=city, state=state, pin= pin)
        add_salesperson.save()
        #pan number must be unique it is not for now 
        return redirect('list_salesperson')

def list_salesperson(request):
    list_salesperson = Add_SalesPerson.objects.all()
    return render(request, 'baseapp/admin/list_salesperson.html',context={"all_salesperson": list_salesperson})

def employee_review(request):
    return render(request,'baseapp/admin/employee_review.html')

def confirmed_bookings(request):
    confirmed_bookings = Booking.objects.all()
    return render(request, 'baseapp/admin/confirmed_bookings.html',context={"confirmed_bookings": confirmed_bookings})

def add_sites(request):
    if(request.method =="GET"):
        return render(request, 'baseapp/admin/add_sites.html')
    if(request.method=="POST"):
        site_name = request.POST['site_name']
        img = File(request.FILES.get('img'))
        property_type = request.POST['property_type']
        location = request.POST['location']

       
        
        add_sites = Add_Sites(site_name = site_name, img = img, property_type = property_type, location = location)
        add_sites.save()
        #pan number must be unique it is not for now 
        return redirect('ongoing_sites')

    


def ongoing_sites(request):
    ongoing_sites = Add_Sites.objects.all()
    return render(request, 'baseapp/admin/ongoing_sites.html',context={"all_sites": ongoing_sites})



