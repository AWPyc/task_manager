from django.db import models
from users.models import User

# Create your models here.
class Project(models.Model):
    VISIBILITY_CHOICES = [
        ("no_restrictions", "No restrictions"),
        ("restricted", "Restricted")
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    members = models.ManyToManyField(User, related_name='projects', blank=True, null=True)
    visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, blank=True, null=False,
                                  default="no_restrictions")

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To do'),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    task_creator = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='task_creator', null=True)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', null=False)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='tasks', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=False)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, blank=False)
    deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
