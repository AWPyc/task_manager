from rest_framework import serializers
from users.models import User
from .models import Project, Task
import datetime

class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), write_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    members_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = ['name', 'description', 'owner', 'members', 'members_info']

    def get_members_info(self, obj):
        return [{"id": user.id, "username": user.username} for user in obj.members.all()]

class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(many=False, queryset=Project.objects.all(), write_only=True)
    task_creator = serializers.ReadOnlyField(source='task_creator.username')
    project_name = serializers.ReadOnlyField(source='project.name')

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['task_creator']

    def validate_deadline(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError("Deadline must be later than today's date")
        return value

    def validate_project(self, value):
        request = self.context['request']
        if not value.owner == request.user and request.user not in value.members.all():
                raise serializers.ValidationError("User must be an owner or a member of the selected project!")
        return value