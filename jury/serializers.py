from rest_framework import serializers
from .models import UserProfile, UserProject

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = ('__all__')

class UserProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProject
    fields = ('__all__')
