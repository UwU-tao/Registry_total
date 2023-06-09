from django.contrib import admin
from .models import Vehicle, Owner, VehicleRegistration
from import_export.admin import ImportExportModelAdmin

# @admin.register(Owner)
# class OwnerAdmin(ImportExportModelAdmin):
#     list_display = ('name', 'email', 'location')

# @admin.register(Vehicle)
# class OwnerAdmin(ImportExportModelAdmin):
#     list_display = ('name', 'email', 'location')
    
@admin.register(VehicleRegistration)
class OwnerAdmin(ImportExportModelAdmin):
    list_display = ('regis_date', 'expiration_date', 'regis_center')