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
        fields = ['id', 'name', 'description', 'owner', 'members', 'visibility', 'members_info']

    def get_members_info(self, obj):
        return [{"id": user.id, "username": user.username} for user in obj.members.all()]


class ProjectSummarySerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'tasks']

    def get_tasks(self, obj):
        user = self.context.get("user")
        tasks = obj.tasks.filter(assigned_to=user)
        return TaskSummarySerializer(tasks, many=True).data


class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(many=False, queryset=Project.objects.all(), write_only=True)
    task_creator = serializers.ReadOnlyField(source='task_creator.username')
    project_name = serializers.ReadOnlyField(source='project.name')

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['task_creator']

    def validate_deadline(self, value):
        if value is None:
            return value
        elif value < datetime.date.today():
            raise serializers.ValidationError("Deadline must be later than today's date")
        return value

    def validate_project(self, value):
        request = self.context['request']
        if not value.owner == request.user and request.user not in value.members.all():
                raise serializers.ValidationError("User must be an owner or a member of the selected project!")
        return value

    def validate(self, attrs):
        project = attrs.get("project")
        assigned_to = attrs.get("assigned_to")

        if assigned_to is None:
            return attrs

        if not assigned_to in project.members.all():
            raise serializers.ValidationError({"assigned_to": "Assigned user must be a member of the selected project!"})

        return attrs


class TaskSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'status', 'deadline']