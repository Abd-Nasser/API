from django.contrib import admin
from .models import Profils

@admin.register(Profils)
class AdminProfil(admin.ModelAdmin):
    list_display = ["nom", "prenom", "article", "montant", "status", "create_at"]
    list_filter = ["article"]
    search_fields = ["nom", "prenom", "article", "montant",]



 
