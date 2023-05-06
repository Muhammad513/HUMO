from django.db import models
from .choices import tr_marka
import os
import datetime
from login.models import Profile



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
    fizlitsa=models.OneToOneField('Fizlitsa',on_delete=models.PROTECT,null=True)
    bolim=models.ForeignKey('Bolim',on_delete=models.PROTECT)
    lavozim=models.ForeignKey('Lavozim',on_delete=models.PROTECT,null=True)
    pasport=models.OneToOneField('Pasport',on_delete=models.PROTECT)
    card=models.OneToOneField('Card',on_delete=models.PROTECT,null=True)
    hodim=models.OneToOneField('login.Profile',on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self) -> str:
        return f'{self.fizlitsa.f_name} {self.fizlitsa.l_name} {self.fizlitsa.ful_name}'

    def old(self):
        year=datetime.now().strftime("%Y")
        birth=self.fizlitsa.birth-year
        return birth


class Lavozim(models.Model):
    lavozim=models.CharField(max_length=50)
    def __str__(self) -> str:
        return str(self.lavozim)    
    
class Fizlitsa(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    ful_name=models.CharField(max_length=50)    
    birth=models.DateField()

class Pasport(models.Model):
    seriya=models.CharField(max_length=2)
    raqami=models.CharField(max_length=9)
    jshir=models.CharField(max_length=14)
    data1=models.DateField()
    data2=models.DateField()

class Bolim(models.Model):
    bolim=models.CharField(max_length=30)

    def __str__(self) -> str:
        return str(self.bolim)
class Card(models.Model):
    raqami=models.CharField(max_length=16)
    mudati=models.CharField(max_length=7)    
