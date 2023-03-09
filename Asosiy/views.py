from django.db.models import Avg
from django.shortcuts import render,redirect
from django.views import View
from .models import *



class Home2View(View):
    def get(self,request):
        return render(request, 'page-index-2.html')


class HomeView(View):
    def get(self,request):
        data = {"bolimlar":Bolim.objects.all()[:7],
                "Chegirmalilar":Mahsulot.objects.filter(chegirma__gt=0).order_by('-chegirma')[:5]}
        return render(request,'page-index.html',data)


class BolimlarView(View):
    def get(self,request):
        data = {'hamabolimlar':Bolim.objects.all()}
        return render(request,'page-category.html',data)


class BolimMahsulotarView(View):
    def get(self,request,pk):
        b1 = Bolim.objects.get(id=pk)
        data = {'bitamahsulot':Mahsulot.objects.filter(Bolim=b1)}
        return render(request,'page-listing-grid.html',data)


class MahsulotarView(View):
    def get(self,request,pk):
        izohlar = Izoh.objects.filter(mahsulot__id=pk)
        ortachasi = izohlar.aggregate(Avg('baho')).get('baho__avg')
        if ortachasi:
            ortachasi *= 20
        else:
            ortachasi = 0
        data = {"mahsulot":Mahsulot.objects.get(id=pk),
                "media":Media.objects.filter(Mahsulot__id=pk),
                "izohlar":izohlar,
                "izohlar_soni":izohlar.count(),
                "ortachasi":ortachasi*20
                }
        return render(request,"page-detail-product.html",data)
    def post(self,request,pk):
        Izoh.objects.create(
            baho = request.POST.get('rating'),
            matn = request.POST.get('comment'),
            profil = Profil.objects.get(user=request.user),
            mahsulot = Mahsulot.objects.get(id=pk),
        )
        return redirect(f'/Asosiy/mahsulot/{pk}')