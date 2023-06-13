from rest_framework import serializers
from .models import Owner, Vehicle, VehicleRegistration
from django.contrib.auth.models import User
from myapp.models import Vehicle, VehicleRegistration

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        # first_name=validated_data['first_name'],
    )
        user.set_password(validated_data['password'])
        user.save()
        return user

class VehicleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vehicle
        fields = ['plate', 'regis_date', 'province', 'type', 'brand', 'model_code', 'man_year', 'man_country', 'engine_no', 'chassis_no', 'color', 'sit', 'load', 'modification', 'lifetime_limit', 'regis_code', 'purpose']


        
class VehicleRegisSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)
    
    class Meta:
        model = VehicleRegistration
        fields = ['codee', 'regis_date', 'expiration_date', 'regis_center', 'vehicle', 'my_plate']
        
class OwnerSerializer(serializers.ModelSerializer):
    regis = VehicleRegisSerializer(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ['idd', 'first_name', 'last_name', 'email', 'phone', 'address', 'dob', 'regis']