from django.db import models

# Create your models here.

class Paciente(models.Model):
    img = models.FileField(upload_to="images/", default="")
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
