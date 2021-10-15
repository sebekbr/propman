from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(HousingAssociation)
admin.site.register(Tenants)
admin.site.register(Landlords)
admin.site.register(Property)
admin.site.register(LeaseAgreement)
admin.site.register(BillVendors)
admin.site.register(Bills)