from django.db import models
from .choices import tr_marka
class GBrigada(models.Model):
    br_num=models.CharField(max_length=2)
    massiv=models.ForeignKey('Massiv',on_delete=models.PROTECT)
    hudud=models.ForeignKey('Hudud',on_delete=models.PROTECT)
    brigadir=models.CharField(max_length=30)
    gektar=models.FloatField()
    reja=models.FloatField()

    def __str__(self):
        return self.br_num

class Galla(models.Model):
    date=models.DateField(null=True)
    brigada=models.ForeignKey('GBrigada',on_delete=models.PROTECT,null=True)
    sofVazn=models.IntegerField(blank=True)
    ombor=models.ForeignKey("OmborG",on_delete=models.CASCADE,blank=True)
    yuk_num=models.CharField(max_length=3,blank=True)
    tr_marka=models.CharField(max_length=20,choices=tr_marka,blank=True)
    tr_num=models.CharField(max_length=20,blank=True)
    tr_name=models.CharField(max_length=30,null=True,blank=True)
    imzo=models.BooleanField(default=False)

    def __str__(self):
        return str(self.sofVazn)


class OmborG(models.Model):
    name=models.CharField(max_length=30)
    reja=models.FloatField(null=True)
    sentner=models.FloatField(null=True)

    def __str__(self):
        return str(self.name)




class Massiv(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name




class Hudud(models.Model):
    h_num=models.CharField(max_length=1)
    Agranom_full_name=models.CharField(max_length=200)
    
    
    def __str__(self):
        return str(self.Agranom_full_name)

