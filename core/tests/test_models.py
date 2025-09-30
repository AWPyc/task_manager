import pytest
import datetime
from projects.models import Project, Task

@pytest.mark.django_db
def test_project_default_visibility(user):
    project = Project.objects.create(name="Test", owner=user)
    assert project.visibility == "no_restrictions"

@pytest.mark.django_db
def test_task_deadline_validation(user, project):
    task = Task.objects.create(
        title="Test Task",
        project=project,
        task_creator=user,
        status="todo",
        priority="low",
        deadline=datetime.date.today() + datetime.timedelta(days=1),
    )
    assert task.deadline >= datetime.date.today()
