from django.contrib import admin
from .models import Perfil

# Register your models here.
class PerfilAdmin(admin.ModelAdmin):
    fields = ['user','bio','f_nacimiento','foto_perfil', 'seguidor']

admin.site.register(Perfil, PerfilAdmin)