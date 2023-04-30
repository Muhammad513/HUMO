from django.contrib import admin
from .models import*
# Register your models here.

class GbrigadaAdmin(admin.ModelAdmin):
    list_display=('br_num','massiv','brigadir','hudud','gektar','reja',)

class GallaAdmin(admin.ModelAdmin):
    list_display=('date','brigada','sofVazn','ombor','yuk_num','tr_marka','tr_num','tr_name','imzo')


admin.site.register(Galla,GallaAdmin)
admin.site.register(GBrigada,GbrigadaAdmin)


admin.site.register([Hudud,Massiv,OmborG,Pasport,Lavozim])

from django_reverse_admin import ReverseModelAdmin


class HodimAdmin(ReverseModelAdmin):
    inline_type = 'stacked'
    inline_reverse = [
                      ('fizlitsa', {'fields': ['f_name','l_name','ful_name','birth']}),
                      ('pasport', {'fields': ['seriya','raqami','jshir','data1','data2']}),
                      ('card', {'fields': ['raqami','mudati']}),
                      
                      ]
admin.site.register(Hodim, HodimAdmin)