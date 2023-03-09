from django.db import models
from User.models import Profil

class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to="bolimlar")
    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=200)
    narx = models.FloatField()
    brend = models.CharField(max_length=100)
    davlat = models.CharField(max_length=100)
    kafolat = models.CharField(max_length=20)
    ninimum_miqdor = models.PositiveSmallIntegerField(default=1)
    tasdiqlangan = models.BooleanField(default=True)
    yetkazib_berish = models.CharField(max_length=15)
    mavjud = models.BooleanField(default=True)
    chegirma = models.PositiveSmallIntegerField(default=0)
    Bolim = models.ForeignKey(Bolim,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nom}, {self.brend}'

class Media(models.Model):
    rasm = models.FileField(upload_to="mahsulotlar")
    Mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)


class Izoh(models.Model):
    baho = models.CharField(max_length=10)
    matn = models.CharField(max_length=50)
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE,null=True)
    sana = models.DateField()
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE)
    def __str__(self):
        return self.baho


