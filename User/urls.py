from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Loginview.as_view(), name='login'),
    path('register/', Registerview.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]