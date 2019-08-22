from apiDetails.models import Bankings_info
from rest_framework import serializers

class bankSerializer(serializers.ModelSerializer):

    class Meta:
        model=Bankings_info
        fields= '__all__'