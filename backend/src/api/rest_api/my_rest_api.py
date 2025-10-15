from api.models import Profils
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.rest_api.serializers import ProfilsSerializers1, ProfilsSerializers2
from django.shortcuts import get_object_or_404


@api_view(["GET", "POST", "PUT", "DELETE", "PATCH"])
def profils_api_view(request, pk=None): 
    
    if request.method == "GET":
        if pk:
            profil = get_object_or_404(Profils, pk=pk)
            serializerprofil = ProfilsSerializers2(profil)
            return Response(serializerprofil.data, status=status.HTTP_200_OK)
            
        all_profils = Profils.objects.all()
        serializer = ProfilsSerializers2(all_profils, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
    elif request.method == 'POST':
        serializer = ProfilsSerializers1(data=request.data)
        if serializer.is_valid():
            serial_save = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method =='PUT':
        if pk:
            updatprofil = get_object_or_404(Profils, pk=pk)
            updatprofilserializer = ProfilsSerializers1( updatprofil, data=request.data)
            if updatprofilserializer.is_valid(raise_exception=True):
                updatprofilserializer.save()
                return Response(updatprofilserializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(updatprofilserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Pk is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        
    elif request.method == "PATCH":
        if pk:
            pathupdateprofil = get_object_or_404(Profils, pk=pk)
            pathupdateserializer = ProfilsSerializers1(pathupdateprofil, data=request.data, partial=True)
            if pathupdateserializer.is_valid():
                pathupdateserializer.save()
                return Response(pathupdateserializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(pathupdateserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Pk is required"}, status=status.HTTP_400_BAD_REQUEST)
        
    
    elif request.method == 'DELETE':
        if pk:
            deleteprofil = get_object_or_404(Profils, pk=pk)
            all_profils = Profils.objects.all()
            serializer = ProfilsSerializers2(all_profils, many=True)
            deleteprofil.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Pk is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        
    
        
        
    
        


       
    
      
    
        
    