from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view(), name="user_detail"),
    path('users/new/', views.CreateUserView.as_view()),   
]

urlpatterns = format_suffix_patterns(urlpatterns)