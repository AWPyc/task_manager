from .models import Task, Project
import django_filters
from users.models import User

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=Task._meta.get_field('status').choices)
    priority = django_filters.ChoiceFilter(choices=Task._meta.get_field('priority').choices)
    assigned_to = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    project = django_filters.ModelChoiceFilter(queryset=Project.objects.all())

    class Meta:
        model = Task
        fields = ['status', 'priority', 'assigned_to', 'project']

