from django.urls import path
from .views import RegistrationUserView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegistrationUserView.as_view(), name='register'),
    path('token/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]