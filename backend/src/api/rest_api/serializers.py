from api.models import Profils
from rest_framework import serializers

class ProfilsSerializers1(serializers.ModelSerializer):
    name = serializers.CharField()
    montant = serializers.IntegerField()
    montant_in_euros = serializers.SerializerMethodField()
    descriptions = serializers.SerializerMethodField()
    profil_url = serializers.HyperlinkedIdentityField(view_name='my_first_api:first-api', lookup_field="pk")

    class Meta:
        model = Profils
        fields = ["id","name", "prenom", "article", "montant", "montant_in_euros", "descriptions", "profil_url",]
        read_only_fields = ["create_at", "status"]
        
    
    def get_montant_in_euros(self, obj): 
        return obj.get_montant_in_euros()
    
    def get_descriptions(self, obj):
        return obj.get_descriptions()
    
    #def get_profil_url(self, obj):
        #return obj.get_absolute_url()
            
    
    ################### data validation serializers side 
    def validate_nom (self, value):
        if value in ["le clown", "indésirable", "far_man"]:
            raise serializers.ValidationError({"message":f"the name <<{value}>> is in the list of ban person "})
        
 

class ProfilsSerializers2(serializers.Serializer):
    name = serializers.CharField()
    prenom = serializers.CharField()
    article = serializers.CharField()
    montant = serializers.IntegerField()
    