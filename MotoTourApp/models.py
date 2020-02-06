from django.db import models

# Create your models here.
from django.db import models


class Post(models.Model):
    nom = models.CharField(max_length=120, help_text='Nom du participant')
    prenom = models.CharField(max_length=120, help_text="Prenom du participant")
    age = models.CharField(max_length=120, help_text="age du participant")
    sexe = models.CharField(max_length=120, help_text="sexe du participant")
    marque_moto = models.CharField(max_length=120, help_text="marque de la moto")
    cylindré = models.CharField(max_length=120, help_text="cylindré de la moto")
    kilometrage = models.CharField(max_length=120, help_text="kilometrage de la moto")

    def __str__(self):
        return self.nom
