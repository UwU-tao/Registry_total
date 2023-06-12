from django.db import models
from datetime import datetime

class Owner(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    idd = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    dob = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'    

class VehicleRegistration(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    codee = models.CharField(max_length=50)
    regis_date = models.CharField(max_length=50)
    expiration_date = models.CharField(max_length=50)
    regis_center = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    # vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.owner} - {self.vehicle}'
    
class Vehicle(models.Model):
    license_plate = models.CharField(primary_key=True, max_length=50)
    plate = models.CharField(max_length=50)
    regis_date = models.CharField(max_length=20)
    province = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model_code = models.CharField(max_length=50)
    man_year = models.CharField(max_length=50)
    man_country = models.CharField(max_length=50)
    engine_no = models.CharField(max_length=50)
    chassis_no = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    sit = models.CharField(max_length=10)
    load = models.CharField(max_length=10, blank=True, null=True)
    modification = models.CharField(max_length=50, blank=True, null=True)
    lifetime_limit = models.CharField(max_length=20, null=True, blank=True)
    purpose = models.CharField(max_length=100, null=True, blank=True)    
    regis_code = models.ForeignKey(VehicleRegistration, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'
