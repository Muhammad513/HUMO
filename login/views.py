from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .form import ProfileForm,NaryadForm
from .models import*
from .function import*
from homes.models import*
from django.forms import formset_factory,modelformset_factory
from datetime import datetime

def loginPage(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,"login ёки парол нотугри")    
    return render(request,"login/login.html")

def logoutUser(request):
    logout(request)
    return redirect('login')





def setting(request):
    user=request.user.profile.id
    profile=Profile.objects.get(id=user)
    form=ProfileForm(instance=profile)
    if request.method == "POST":
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('setting')
    
    context={"form":form,"profile":profile}
    return render(request,'homes/setting.html',context)




def paxta(request):
    
    
    return render(request,'homes/paxta.html')

def galla(request):
    date=request.GET.get("date")
    date=datenow(date)    
    #-1 Hudud
    br_item_1=item_hudud_G(GBrigada,1)
    birkunda=birkunda_s(GBrigada,1,date)
    hudud_1=zip(br_item_1,birkunda)
    br_itemsm_1=item_hudud_G(GBrigada,1)
    birkundasm=birkunda_s(GBrigada,1,date)
    hududsm_1=zip(br_itemsm_1,birkundasm)
    
    
    #-2 Hudud
    br_item_2=item_hudud_G(GBrigada,2)
    birkunda=birkunda_s(GBrigada,2,date)
    hudud_2=zip(br_item_2,birkunda)
    br_itemsm_2=item_hudud_G(GBrigada,2)
    birkundasm=birkunda_s(GBrigada,2,date)
    hududsm_2=zip(br_itemsm_2,birkundasm)
    
    #-3 Hudud
    br_item_3=item_hudud_G(GBrigada,3)
    birkunda=birkunda_s(GBrigada,3,date)
    hudud_3=zip(br_item_3,birkunda)
    br_itemsm_3=item_hudud_G(GBrigada,3)
    birkundasm=birkunda_s(GBrigada,3,date)
    hududsm_3=zip(br_item_3,birkunda)
    
    
    context={"hudud_1":hudud_1,"hudud_2":hudud_2,"hudud_3":hudud_3,"date":date,
             'hududsm_1':hududsm_1,'hududsm_2':hududsm_2,'hududsm_3':hududsm_3}
    return render(request,'homes/galla/galla.html',context)


def ombor(request):
    
    dmk1=item_ombor_G(OmborG,"DMK-1")
    dmk2=item_ombor_G(OmborG,"DMK-2")
    zavod=item_ombor_G(OmborG,"ZAVOD")
    context={"dmk1":dmk1,'dmk2':dmk2,"zavod":zavod}
    return render(request,'homes/dmk.html',context)

def reestr(request):
    res=Galla.objects.all().order_by('-date').values('date','brigada','brutto','tara','ombor__name','yuk_num','tr_num','tr_marka','tr_name','imzo','sofVazn')
    context={'res':res}
    return render(request,'homes/restr.html',context)    



def kadr(request):
    kadr=Hodim.objects.all().order_by('bolim')
    
    context={"kadr":kadr}
    
    return render(request,'kadr/kadr-inc.html',context)        


def tavalud(request):
    dates=datetime.now().strftime("%d.%m")
    tavalud=Hodim.objects.all()
    
    context={"tavalud":tavalud,"dates":dates}
    
    return render(request,'kadr/tavalud.html',context)        