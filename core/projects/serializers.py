from rest_framework import serializers
from users.models import User
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username') # tej lini dobrze nie rozumiem, czym jest source tak wlasciwie?

    class Meta:
        model = Project
        fields = ['name', 'description', 'owner', 'members']
