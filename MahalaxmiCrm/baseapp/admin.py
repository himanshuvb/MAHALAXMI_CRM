from django.contrib import admin
from .models import Agreement, Amenities, Client, Agent,Payment, Project, Properties, Property_Type, Source


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