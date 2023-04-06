from django.contrib import admin
from .models import Vehicle, Owner, VehicleRegistration
# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Owner)
admin.site.register(VehicleRegistration)