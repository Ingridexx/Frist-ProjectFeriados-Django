from rest_framework import serializers
from .models import Holiday

class HolidaySerializer(serializers.ModelSerializer): # Define como o modelo Holiday será convertido para JSON e vice-versa.
    class Meta: 
        model = Holiday
        fields = '__all__' #Inclui todos os campos do modelo no serializer 
        