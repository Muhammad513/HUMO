from django.db import models
from .choices import tr_marka
import os
import datetime



def get_image_path(instance,filename):
    return os.path.join('Hodimlar', str(instance.id),filename)
    
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
    date=models.DateField()
    brigada=models.ForeignKey('GBrigada',on_delete=models.PROTECT)
    ombor=models.ForeignKey("OmborG",on_delete=models.CASCADE)
    yuk_num=models.CharField(max_length=3)
    tr_marka=models.CharField(max_length=20,choices=tr_marka)
    tr_num=models.CharField(max_length=20)
    tr_name=models.CharField(max_length=30)
    imzo=models.BooleanField(default=False)
    brutto=models.FloatField(null=True,blank=True)
    tara=models.FloatField(null=True,blank=True)
    sofVazn=models.IntegerField(blank=True,null=True,default=0)

    def __str__(self):
        return str(self.sofVazn)

    def save(self,*args,**kwargs):
        if self.brutto!=None and self.tara!=None:
            self.sofVazn=round(self.brutto-self.tara,1)
            
        super().save(*args,**kwargs)

    


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

class Hodim(models.Model):
    
