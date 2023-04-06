from django.urls import path,include
from .views import loginPage,logoutUser,setting,paxta,galla


urlpatterns = [
    path('',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('setting',setting,name='setting'),
    path('galla/',galla,name='galla'),
    path('paxta/',paxta,name='paxta'),
]
