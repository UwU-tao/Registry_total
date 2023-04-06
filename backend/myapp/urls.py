from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.home, name='home'),  
    # path('account/login', views.login, name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('home/', views.home, name='home'),
]
