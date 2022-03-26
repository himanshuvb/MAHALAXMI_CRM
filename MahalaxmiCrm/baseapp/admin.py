from django.contrib import admin
from .models import Client, Agent,Payment


# Register your models here.
admin.site.register(Client)
admin.site.register(Agent)
admin.site.register(Payment)