from .models import*
from django.db.models import Sum,Count,Q
from django.db.models import  F,IntegerField,FloatField
import datetime
from django.db.models import Sum,Count,F,Q

def datenow(date):
    if date is None:
        x=datetime.datetime.now()
        date=x.strftime("%Y-%m-%d")
    else:
        date=date
    return date    



def item_hudud_G(obj,num_hudud):
    result=obj.objects.filter(hudud__h_num=num_hudud).annotate(
                        br_sums=Sum(F('galla__sofVazn')/1000, output_field=FloatField()),
                        sent=Sum(F('galla__sofVazn')/F("gektar")/100, output_field=FloatField()),
                        bajarilish=Sum(F('galla__sofVazn')/10/F("reja"), output_field=FloatField())
                    )
    
    result=result.values("br_sums","br_num","massiv__name","brigadir","gektar","reja","sent","bajarilish")                    
    return result

def birkunda_s(obj,num_hudud,date):
    result=obj.objects.filter(hudud__h_num=num_hudud).annotate(
                        birkunda=Sum(F('galla__sofVazn')/1000,filter=Q(galla__date=date), output_field=FloatField()),
                    )
    
    result=result.values('birkunda')                    
    return result
