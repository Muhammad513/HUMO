from django.urls import path,include
from .views import loginPage,logoutUser,setting,bolim,naryad


urlpatterns = [
    path('',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('setting',setting,name='setting'),
    path('galla/',naryad,name='galla'),
]
