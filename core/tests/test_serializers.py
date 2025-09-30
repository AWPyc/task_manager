import pytest
import datetime
from projects.serializers import TaskSerializer
from rest_framework.test import APIRequestFactory

@pytest.mark.django_db
def test_task_serializer_deadline_validation(user, project):
    factory = APIRequestFactory()
    request = factory.post('/tasks/')
    request.user = user

    serializer = TaskSerializer(
        data={
            "title": "Invalid Task",
            "task_creator": user,
            "status": "todo",
            "priority": "low",
            "project": project.id,
            "deadline": datetime.date.today() - datetime.timedelta(days=1),
        },
        context={"request": request},
    )

    assert not serializer.is_valid()
    assert "deadline" in serializer.errors
