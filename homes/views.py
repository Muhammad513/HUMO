from django.shortcuts import render
from .models import*
from login.function import sana_chart
from django.db.models import Sum,Count,Q
def homes(request):
    context={}
    return render(request,'homes/homes.html',context)



