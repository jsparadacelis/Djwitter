from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    
    perfil = models.ForeignKey("users.Perfil", on_delete=models.CASCADE)
    texto = models.CharField(max_length=140)
    f_escrito = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.texto