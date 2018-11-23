from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300)
    f_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    f_creacion = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user.username
    