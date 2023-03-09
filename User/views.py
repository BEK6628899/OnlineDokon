from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *



class Loginview(View):
    def get(self,request):
        return render(request,'page-user-login.html')
    def post(self,request):
        user = authenticate(
            username = request.POST.get('l'),
            password = request.POST.get('p'),
        )
        if user is None:
            return redirect('/User/login/')
        return redirect('/Asosiy/home/')


class Registerview(View):
    def get(self,request):
        return render(request,'page-user-register.html')
    def post(self,request):
        User.objects.create_user(
            username = request.POST.get('e'),
            password = request.POST.get('c_p')
        )
        return redirect('/User/login/')



class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')

