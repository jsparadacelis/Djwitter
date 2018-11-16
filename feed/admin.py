from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ['perfil','texto']

admin.site.register(Post, PostAdmin)