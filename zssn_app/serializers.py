from rest_framework import serializers
from . models import Survivors


class SurvivorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Survivors
        # fields = ('firstname', 'age')
        fields = '__all__'

class SurvivorsSerializerLocation(serializers.ModelSerializer):

    class Meta:
        model = Survivors
        fields = ('latitude', 'longitude')