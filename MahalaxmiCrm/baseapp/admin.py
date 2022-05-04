from django.contrib import admin
from .models import Add_Sites, Add_Telecaller, Agreement, Amenities, Booking, Client, Agent, FollowUps_Telecaller, NewLead_Telecaller,Payment, Project, Properties, Property_Type, Source, Add_SalesPerson, Visit_Telecaller


# Register your models here.
admin.site.register(Client)
admin.site.register(Agent)
admin.site.register(Payment)
admin.site.register(Properties)
admin.site.register(Agreement)
admin.site.register(Project)
#Masters --> Add_source
admin.site.register(Source)
admin.site.register(Property_Type)
admin.site.register(Amenities)
#Admin 
admin.site.register(Add_Telecaller)
admin.site.register(Add_SalesPerson)
admin.site.register(Add_Sites)
#Telecaller
admin.site.register(NewLead_Telecaller)
admin.site.register(FollowUps_Telecaller)
admin.site.register(Visit_Telecaller)
admin.site.register(Booking)