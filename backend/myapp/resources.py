from import_export import resources
from .models import Owner, Vehicle, VehicleRegistration

class OwnerResource(resources.ModelResource):
    class Meta:
        model = Owner
        
class VehicleResource(resources.ModelResource):
    class Meta:
        model = Vehicle
        
class VehicleRegisResource(resources.ModelResource):
    class Meta:
        model = VehicleRegistration