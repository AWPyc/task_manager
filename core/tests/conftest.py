import pytest
import datetime
from users.models import User
from projects.models import Project, Task

@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="pass123")

@pytest.fixture
def project(user):
    return Project.objects.create(name="Project1", owner=user)

@pytest.fixture
def task(user, project):
    return Task.objects.create(
        title="Task1",
        project=project,
        task_creator=user,
        status="todo",
        priority="low",
        deadline=datetime.date.today() + datetime.timedelta(days=1),
    )
