from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Owner, Vehicle, VehicleRegistration
from django.contrib.auth.decorators import login_required

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'registration/login.html')

@login_required
def home(request):
    return render(request, 'myapp/home.html', {'username': request.user.username})

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
    success_url = reverse_lazy('owner_list')

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
    success_url = reverse_lazy('vehicle_list')

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
    success_url = reverse_lazy('registration_list')
