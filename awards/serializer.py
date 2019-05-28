from rest_framework import serializers
from .models import Project,Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','description','link')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio','contact')        
