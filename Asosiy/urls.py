from django.urls import path
from .views import *

urlpatterns = [
    path('home/',HomeView.as_view(), name='home'),
    path('category/',BolimlarView.as_view(), name='bolimlar'),
    path('bolim/<int:pk>/',BolimMahsulotarView.as_view(), name='bolimlar'),
    path('mahsulot/<int:pk>/',MahsulotarView.as_view(), name='bolimlar'),
]





