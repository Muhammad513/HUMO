from .models import*

class GallaService:
    @classmethod
    def get__galla_list(cls,field):
        return Galla.objects.filter(imzo=True).values_list(*field)
