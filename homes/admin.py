from django.contrib import admin
from .models import Hudud,Massiv,GBrigada,Galla,OmborG
# Register your models here.

class GbrigadaAdmin(admin.ModelAdmin):
    list_display=('br_num','massiv','brigadir','hudud','gektar','reja',)

class GallaAdmin(admin.ModelAdmin):
    list_display=('date','brigada','sofVazn','ombor','yuk_num','tr_marka','tr_num','tr_name','imzo')



admin.site.register(Galla,GallaAdmin)
admin.site.register(GBrigada,GbrigadaAdmin)



admin.site.register([Hudud,Massiv,OmborG])