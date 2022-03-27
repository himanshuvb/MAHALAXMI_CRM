from django.contrib import admin
from .models import Agreement, Client, Agent,Payment, Properties, Source


# Register your models here.
admin.site.register(Client)
admin.site.register(Agent)
admin.site.register(Payment)
admin.site.register(Properties)
admin.site.register(Agreement)
#Masters --> Add_source
admin.site.register(Source)