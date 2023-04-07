from django.urls import path,include
from .views import loginPage,logoutUser,setting,paxta,galla,ombor,reestr


urlpatterns = [
    path('',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('setting',setting,name='setting'),
    path('galla/',galla,name='galla'),
    path('paxta/',paxta,name='paxta'),
    path('ombor/',ombor,name='ombor'),
    path('reestr/',reestr,name='reestr'),
]
