from django.shortcuts import render
from django.http import JsonResponse
from .models import Profils
from django.views.decorators.csrf import csrf_exempt
import json



@csrf_exempt
def my_first_api(request):
    headers = request.headers
    param = request.GET.get("q")
   
    #serialisation manuel
    if request.method == 'POST':
        data =  request.body
        data_jsoner = json.loads(data)
        new_profils = Profils.objects.create(
                                        nom= data_jsoner["nom"],
                                        prenom= data_jsoner["prenom"],
                                        article= data_jsoner["article"],
                                        montant= data_jsoner["montant"]
                                            
            )
        new_profils.save()
        print("c'est creer et savec")
        
        return JsonResponse({
                "nom": new_profils.nom,
                 "prenom": new_profils.prenom,
                 "article": new_profils.article,
                 "montant": new_profils.montant,
                             
            })
        
        #Deserialisation manuel
    else:
        all_profils = Profils.objects.all()
        data = [{
            "nom":profil.nom,
            "prenom": profil.prenom,
            "article": profil.article,
            "montant": profil.montant,
                 }for profil in all_profils]
        return JsonResponse(data, safe=False)
 
       
    
       
