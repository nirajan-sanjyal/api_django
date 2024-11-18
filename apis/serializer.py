from rest_framework import serializers

from apis.models import GeekModels


class GeeksSerializer(serializers.ModelSerializer):

    class Meta:
        model=GeekModels
        fields= '__all__'