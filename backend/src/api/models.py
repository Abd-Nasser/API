from django.db import models

class Profils(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    prenom = models.CharField(max_length=100)
    article = models.CharField(max_length=100)
    montant = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField( auto_now_add=True)
    
    
    def get_montant_in_euros(self):
        return f"{self.montant*656} €"
    
    def get_descriptions(self):
        return f'{self.status}--{self.create_at}'
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('my_first_api:first-api', kwargs={"pk":self.pk})
    
    def __str__(self):
        return f'{self.name} -- {self.prenom}'

 