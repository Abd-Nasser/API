from api.models import Profils
from rest_framework import serializers

class ProfilsSerializers1(serializers.ModelSerializer):
    class Meta:
        model = Profils
        fields = "__all__"
        read_only_field = ["create_at", "status"]
        


class ProfilsSerializers2(serializers.Serializer):
    nom = serializers.CharField()
    prenom = serializers.CharField()
    article = serializers.CharField()
    montant = serializers.IntegerField()
    