from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .form import ProfileForm
from .models import*
from .function import*
from homes.models import*
from django.forms import formset_factory,modelformset_factory
from datetime import datetime
from login.form import Gallaform,Gallaimzo
from .decarators import*
from django.contrib.auth.decorators import login_required
from homes.service import GallaService
from homes.utils import write_galla_to_excel
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
    print(User.objects.all().values())
    return render(request,"login/login.html")


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')




@login_required(login_url='login')
def setting(request):
    user=request.user.profile.id
    profile=Profile.objects.get(id=user)
    hodim=Hodim.objects.filter(hodim=profile.id).values('bolim__bolim',
                                                        'pasport__seriya','pasport__raqami','lavozim__lavozim',
                                                        "pasport__jshir",'pasport__data2','card__raqami','card__mudati')
    form=ProfileForm(instance=profile)
    if request.method == "POST":
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('setting')
    
    context={"form":form,"profile":profile,"hodim":hodim}
    return render(request,'homes/setting.html',context)



@login_required(login_url='login')
def paxta(request):
    
    
    return render(request,'404/404.html')

@login_required(login_url='login')
def galla(request):
    date=request.GET.get("date")
    date=datenow(date)
    imzolandi=Galla.objects.filter(imzo=True).count()
    imzosiz=Galla.objects.filter(imzo=False).count()
     
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
    hududsm_3=zip(br_itemsm_3,birkundasm)
    
    
    context={"hudud_1":hudud_1,"hudud_2":hudud_2,"hudud_3":hudud_3,"date":date,
             'hududsm_1':hududsm_1,'hududsm_2':hududsm_2,'hududsm_3':hududsm_3,
             'imzolandi':imzolandi,'imzosiz':imzosiz}
    return render(request,'homes/galla/galla.html',context)


@login_required(login_url='login')
def ombor(request):
    dmk1=item_ombor_G(OmborG,"DMK-1")
    dmk2=item_ombor_G(OmborG,"DMK-BIRJA")
    zavod=item_ombor_G(OmborG,"ZAVOD")
    urug=item_ombor_G(OmborG,"URUG'LIK")
    
    context={"dmk1":dmk1,'dmk2':dmk2,"zavod":zavod,'urug':urug}
    return render(request,'homes/dmk.html',context)

@login_required(login_url='login')
def reestr(request):
    res=Galla.objects.all().order_by('-id').values('date','brigada','brutto','tara','ombor__name','yuk_num','tr_num','tr_marka','tr_name','imzo','sofVazn')
    data_galla=GallaService.get__galla_list(field=['id','date','brigada__br_num','brigada__brigadir','ombor__name','yuk_num','tr_marka','tr_num','tr_name','brutto','tara','sofVazn','sender__username'])
    write_galla_to_excel(file_name='media/xls/galla.xlsx',sheet_name='reestr',gallas_data=data_galla)



    context={'res':res}
    return render(request,'homes/restr.html',context) 







def way(request):
    res=Galla.objects.filter(imzo=True).order_by('-id').values('date','brigada','brutto','tara','ombor__name','yuk_num','tr_num','tr_marka','tr_name','imzo','sofVazn')
    context={'res':res}
    return render(request,'homes/restr.html',context)
def stop(request):
    res=Galla.objects.filter(imzo=False).order_by('-id').values('date','brigada','brutto','tara','ombor__name','yuk_num','tr_num','tr_marka','tr_name','imzo','sofVazn')
    context={'res':res}
    return render(request,'homes/restr.html',context)   


@login_required(login_url='login')
def kadr(request):
    kadr=Hodim.objects.all().order_by('bolim')
    year=datetime.now().strftime("%Y")
   
    context={"kadr":kadr,'year':year}
    return render(request,'kadr/kadr-inc.html',context)        


@login_required(login_url='login')
def tavalud(request):
    dates=datetime.now().strftime("%d.%m")
    year=datetime.now().strftime("%Y")
    tavalud=Hodim.objects.all()
    context={"tavalud":tavalud,"dates":dates,'year':year}
    return render(request,'kadr/tavalud.html',context)        

@login_required(login_url='login')
@allowed_users(allowed_roles=['nazoratchi','admin'])
def gallaform(request):
    sender=request.user
    form=Gallaform()
    if request.method == "POST":
        form=Gallaform(request.POST)
        if form.is_valid():
            forms=form.save(commit=False)
            forms.sender=request.user
            forms.save()
            messages.success(request,"ЮК ХАТИ ЖУНАТИЛДИ")
            return redirect('gallaform')
        else:
            messages.success(request,"ЮК ХАТИ ЖУНАТИЛДИ")
            return redirect('gallaform')
    context={'form':form}
    return render(request,'form/yukhati.html',context)    

@login_required(login_url='login')
@allowed_users(allowed_roles=['Ombor','admin'])
def zavodimzo(request):
    zavod=Galla.objects.filter(ombor__name="ZAVOD",imzo=False).order_by('-id').values('date','brigada','ombor__name','yuk_num','tr_num','tr_marka','tr_name','imzo','id')
    context={'zavod':zavod}
    return render(request,'form/zavodimzo.html',context)    

@login_required(login_url='login')
@allowed_users(allowed_roles=['Ombor','admin'])
def zavodimzopk(request,pk):
    imzo=Galla.objects.get(id=pk)
    form=Gallaimzo(instance=imzo)
    if request.method == "POST":
        form=Gallaimzo(request.POST,instance=imzo)
        if form.is_valid():
            form.save()
            messages.success(request,"ЮК ХАТИ ЖУНАТИЛДИ")
            return redirect('zavodimzo')
    context={"form":form,"imzo":imzo}
    return render(request,'form/zavodimzopk.html',context)    
#------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@allowed_users(allowed_roles=['dmk','admin'])
def dmkimzo(request):
    dmk=Galla.objects.filter(ombor__name__in=['DMK-1',"DMK-BIRJA","URUG'LIK"],imzo=False).order_by('-id').values('date','brigada','ombor__name','yuk_num','tr_num','tr_marka','tr_name','imzo','id')
    context={'dmk':dmk}
    return render(request,'form/dmkimzo.html',context)    


@login_required(login_url='login')
@allowed_users(allowed_roles=['dmk','admin'])
def dmkimzopk(request,pk):
    imzo=Galla.objects.get(id=pk)
    form=Gallaimzo(instance=imzo)
    if request.method == "POST":
        form=Gallaimzo(request.POST,instance=imzo)
        if form.is_valid():
            form.save()
            return redirect('dmkimzo')
    context={"form":form,"imzo":imzo}
    return render(request,'form/dmkimzopk.html',context)    


@login_required(login_url='login')
def ishxaqi(request):
    
    return render(request, '404/404.html')

def plastik(request):
    
    return render(request, '404/404.html')    
from .form import RegistrForm

@login_required(login_url='login')
def reg(request):
    form = RegistrForm()
    if request.method == "POST":
        form=RegistrForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            login(request,user)
            messages.success(request,"muvaffaqiyatli ro'xatdan o'tingiz")
            return redirect('setting')
        else:
            messages.error(request,'Parametrlarni xato berdingiz')
    context={"form":form,}
    

    return render(request, 'login/reg.html',context)        



def yukhatlar(request):
    user=request.user
    dmk=Galla.objects.filter(sender=user).order_by('-id').values('date','brigada','ombor__name','yuk_num','tr_num','tr_marka','tr_name','imzo','id')
    context={'dmk':dmk}
    return render(request,'profile/yukhati.html',context)        