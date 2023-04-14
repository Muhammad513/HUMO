from django.urls import path,include
from .views import*


urlpatterns = [
    path('',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('setting',setting,name='setting'),
    path('galla/',galla,name='galla'),
    path('paxta/',paxta,name='paxta'),
    path('ombor/',ombor,name='ombor'),
    path('reestr/',reestr,name='reestr'),
    path('kadr/',kadr,name='kadr'),
    path('tavalud/',tavalud,name='tavalud'),
    path('adminalla/',gallaform,name='gallaform'),
    path('zavodimzo/',zavodimzo,name='zavodimzo'),
    path('zavodimzo/<str:pk>/',zavodimzopk,name='zavodimzopk'),
     path('dmkimzo/',dmkimzo,name='dmkimzo'),
    path('dmkimzo/<str:pk>/',dmkimzopk,name='dmkimzopk'),


]
