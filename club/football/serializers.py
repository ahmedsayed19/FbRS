from django.db import models
from rest_framework import serializers
from .models import ClubMember, Playgrounds, ReservedHours

class MemeberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubMember
        fields = '__all__'

        # fields = ('id' , 'password' , 'last_login' , 'is_superuser' , 'username' , 'first_name', 'last_name' , 'email' , 'is_staff' , 'is_active' , 'date_joined' , 'profile_pic' , 'phone' , 'is_owner' , 'is_player')
class PGsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playgrounds
        fields = '__all__'

class RHSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservedHours
        fields = '__all__'
