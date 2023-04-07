from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .form import ProfileForm,NaryadForm
from .models import*
from .function import*
from homes.models import*
from django.forms import formset_factory,modelformset_factory
# Create your views here.

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
    brigada=Galla.objects.all()
        
    #-1 Hudud
    br_item_1=item_hudud_G(GBrigada,1)
    print(br_item_1)
    
    context={"br_item_1":br_item_1}
    return render(request,'homes/galla.html',context)
