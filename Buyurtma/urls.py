from django.urls import path
from .views import *

urlpatterns = [
    path('savat/',SavatView.as_view(), name='savat')
]