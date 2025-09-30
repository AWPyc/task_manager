import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_create_project(user):
    client = APIClient()
    client.force_authenticate(user=user)
    resp = client.post("/projects/", {"name": "Proj", "description": "desc"})
    assert resp.status_code == 201
    assert resp.data["name"] == "Proj"

@pytest.mark.django_db
def test_mark_task_as_done(user, project, task):
    client = APIClient()
    client.force_authenticate(user=user)
    resp = client.post(f"/tasks/{task.id}/mark_as_done/")
    assert resp.status_code == 200
    assert resp.data["status"] == "done"
