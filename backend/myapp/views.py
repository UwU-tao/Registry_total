from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Owner, Vehicle, VehicleRegistration
from django.contrib.auth.models import User
from myapp import serializers


from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes = (TokenAuthentication,)

class CreateUserView(generics.CreateAPIView):
    model = User
    serializer_class = serializers.UserSerializer

    def post(self, request, format='json'):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OwnerListView(ListView):
    model = Owner

class OwnerDetailView(DetailView):
    model = Owner

class OwnerCreateView(CreateView):
    model = Owner
    fields = '__all__'

class OwnerUpdateView(UpdateView):
    model = Owner
    fields = '__all__'

class OwnerDeleteView(DeleteView):
    model = Owner

class VehicleListView(ListView):
    model = Vehicle

class VehicleDetailView(DetailView):
    model = Vehicle

class VehicleCreateView(CreateView):
    model = Vehicle
    fields = '__all__'

class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = '__all__'

class VehicleDeleteView(DeleteView):
    model = Vehicle
    

class VehicleRegistrationListView(ListView):
    model = VehicleRegistration

class VehicleRegistrationDetailView(DetailView):
    model = VehicleRegistration

class VehicleRegistrationCreateView(CreateView):
    model = VehicleRegistration
    fields = '__all__'

class VehicleRegistrationUpdateView(UpdateView):
    model = VehicleRegistration
    fields = '__all__'

class VehicleRegistrationDeleteView(DeleteView):
    model = VehicleRegistration
    
