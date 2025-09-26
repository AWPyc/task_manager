from rest_framework import serializers
from .models import User
from projects.serializers import ProjectSummarySerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'bio', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    owned_projects = serializers.SerializerMethodField()
    member_projects = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "date_joined", 'owned_projects',
                  'member_projects']

    def get_owned_projects(self, obj):
        from projects.serializers import ProjectSummarySerializer
        projects = obj.owned_projects.all()
        return ProjectSummarySerializer(projects, context=self.context, many=True).data

    def get_member_projects(self, obj):
        from projects.serializers import ProjectSummarySerializer
        projects = obj.projects.all()
        return ProjectSummarySerializer(projects, context=self.context, many=True).data
