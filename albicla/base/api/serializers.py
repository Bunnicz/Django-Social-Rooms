from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from base.models import Room


# Serializers define the API representation.
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
