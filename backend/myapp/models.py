from django.db import models

class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    vin = models.CharField(max_length=17, unique=True)
    license_plate = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    mileage = models.PositiveIntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'

class VehicleRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    registration_date = models.DateField()
    expiration_date = models.DateField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner} - {self.vehicle}'