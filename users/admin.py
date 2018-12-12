from django.contrib import admin
from .models import Perfil, Follow

# Register your models here.
class PerfilAdmin(admin.ModelAdmin):
    fields = ['user','bio','f_nacimiento','foto_perfil']

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Follow)