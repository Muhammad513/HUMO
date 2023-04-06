from django.db import models

class GBrigada(models.Model):
    br_num=models.CharField(max_length=2)
    massiv=models.ForeignKey('Massiv',on_delete=models.PROTECT)
    hudud=models.ForeignKey('Hudud',on_delete=models.PROTECT)
    brigadir=models.CharField(max_length=20)
    gektar=models.FloatField()
    reja=models.FloatField()




class Massiv(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name




class Hudud(models.Model):
    h_num=models.CharField(max_length=1)
    Agranom_full_name=models.CharField(max_length=200)
    
    
    def __str__(self):
        return str(self.Agranom_full_name)

