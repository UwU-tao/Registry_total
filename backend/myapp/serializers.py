from rest_framework import serializers
from .models import Owner, Vehicle, VehicleRegistration

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleRegistrationSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    vehicle = VehicleSerializer()

    class Meta:
        model = VehicleRegistration
        fields = '__all__'
