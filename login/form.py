from .models import*
from homes.models import*
from django import forms
import datetime
from .views import*

x=datetime.datetime.now()
date=x.strftime("%Y-%m-%d")

class ProfileForm(forms.ModelForm):
    
    
    
    class Meta:
        model=Profile
        fields=('pic','firs_name','last_name')
        widgets={
            'firs_name':forms.TextInput(attrs={'type':'text','class':"form-control"}),
            'last_name':forms.TextInput(attrs={'type':'text','class':"form-control"}),
        }
        def clean_pic(self):
            photo=self.clean_data.get("pic")
            return photo


class Gallaform(forms.ModelForm):
    
    
    class Meta:
        model=Galla
        fields=('date','yuk_num','brigada','ombor','yuk_num','tr_marka','tr_num','tr_name')
        widgets={
            'yuk_num':forms.TextInput(attrs={'type':'number'}),
            'date':forms.TextInput(attrs={'type':'date','value':date}),
        }

class Gallaimzo(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brutto'].required = True
        self.fields['tara'].required = True
        self.fields['imzo'].required = True



    class Meta:
        model=Galla
        fields=('imzo','brutto',"tara")
        
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

  