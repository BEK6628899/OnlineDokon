from django.shortcuts import render
from django.views import View


class SavatView(View):
    def get(self,request):
        return render(request,"")

