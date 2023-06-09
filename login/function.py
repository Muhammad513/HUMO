from .models import*
from django.db.models import Sum,Count,Q
from django.db.models import  F,IntegerField,FloatField
import datetime
from django.db.models import Sum,Count,F,Q,ExpressionWrapper

def datenow(date):
    if date is None:
        x=datetime.datetime.now()
        date=x.strftime("%Y-%m-%d")
    else:
        date=date
    return date    



def item_hudud_G(obj,num_hudud):
    result=obj.objects.filter(hudud__h_num=num_hudud).annotate(
                        br_sums=Sum(F('galla__sofVazn')/1000.000, output_field=FloatField(),filter=Q(galla__imzo=True)),
                        sent=Sum(F('galla__sofVazn')/F("gektar")/100.000, output_field=FloatField(),filter=Q(galla__imzo=True)),
                        bajarilish=Sum(F('galla__sofVazn')/10.000/F("reja"), output_field=FloatField(),filter=Q(galla__imzo=True))
                    )
    
    result=result.values("br_sums","br_num","massiv__name","brigadir","gektar","reja","sent","bajarilish",)                    
    return result

def birkunda_s(obj,num_hudud,date):
    result=obj.objects.filter(hudud__h_num=num_hudud).annotate(
                        birkunda=Sum(F('galla__sofVazn')/1000.000,filter=Q(galla__date=date)&Q(galla__imzo=True), output_field=FloatField()),
                    )
    
    result=result.values('birkunda')                    
    return result
def sana_chart(obj,date):
    sana=[]
    for i in date:
        result=obj.objects.all().annotate(
                        birkunda=Sum(F('sofVazn')/1000.000,filter=Q(date=date)&Q(imzo=True), output_field=FloatField()),
                    )
        sana.append(result)
                      
    return sana    

def item_ombor_G(obj,ombor):
    result=obj.objects.filter(name=ombor).annotate(
                        sums=Sum(F('galla__sofVazn')/1000.000, output_field=FloatField(),filter=Q(galla__imzo=True)),
                        )
    
    result=result.values("sums",'reja',"sentner","name")                    
    return result