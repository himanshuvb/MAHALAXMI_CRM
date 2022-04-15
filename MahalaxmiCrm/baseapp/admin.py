from django.contrib import admin
from .models import Add_Telecaller, Agreement, Amenities, Booking, Client, Agent, NewLead_Telecaller,Payment, Project, Properties, Property_Type, Source, Add_SalesPerson


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
#Telecaller
admin.site.register(NewLead_Telecaller)
#Salesperson
admin.site.register(Booking)