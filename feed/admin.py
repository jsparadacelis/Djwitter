from django.contrib import admin
from .models import Tweet

# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    fields = ['perfil','texto']

admin.site.register(Tweet, TweetAdmin)