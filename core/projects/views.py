from django.shortcuts import render
from rest_framework import viewsets
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .filters import TaskFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = TaskFilter
    ordering_fields = ["deadline", "priority", "created_at"]
    ordering = ["created_at"]
    search_fields = ['title', 'description']

    @action(detail=True, methods=["post"])
    def mark_as_done(self, request, pk=None):
        task = self.get_object()
        if task.status == 'done':
            return Response({"detail": "Task is already marked as done."},
                            status=status.HTTP_409_CONFLICT)
        task.status = 'done'
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(task_creator=self.request.user)
