from django.contrib import admin
from .models import Mechanic,Mechanic_ticket,Expert
# Register your models here.

class Mechanic_all(admin.ModelAdmin):
    list_display = ['name', 'phone_no','mechanic_id','assigned_customer_id','available']

class Expert_all(admin.ModelAdmin):
    list_display = ['name', 'phone_no','e_id','assigned_customer_id','description','skills']

class Mechanic_Ticket(admin.ModelAdmin):
    list_display = ['name', 'phone','location','description','m_id']





admin.site.register(Mechanic_ticket,Mechanic_Ticket)
admin.site.register(Mechanic,Mechanic_all)
admin.site.register(Expert,Expert_all)
