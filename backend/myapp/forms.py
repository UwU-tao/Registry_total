from django import forms
from .models import Owner, Vehicle, VehicleRegistration

class OwnerData(forms.Form):
	class meta:
		model = Owner
		fields = '__all__'
  
class VehicleData(forms.Form):
	class meta:
		model = Vehicle
		fields = '__all__'
  
class VehicleRegisData(forms.Form):
	class meta:
		model = VehicleRegistration
		fields = '__all__'