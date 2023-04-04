from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'role')
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
       
        return user
    
class LessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lession
        fields = ('__all__')


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('__all__')


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('__all__')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')