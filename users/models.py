from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(
        upload_to="media/perfil",
        default = 'media/None/no-img.jpg'
    )
    foto_encabezado = models.ImageField(
        upload_to="media/encabezado",
        null=True
    )
    bio = models.CharField(max_length=300)
    f_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    f_creacion = models.DateTimeField(auto_now=True, auto_now_add=False)
    seguidores = models.ManyToManyField("self", blank = True)


    