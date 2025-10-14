from django.db import models

class Profils(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    article = models.CharField(max_length=100)
    montant = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return f'{self.nom} -- {self.prenom}'

 