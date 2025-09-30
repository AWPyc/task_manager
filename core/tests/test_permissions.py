import pytest
from projects.permissions import IsProjectOwnerOrMember, IsTaskOwnerOrAssigned

@pytest.mark.django_db
def test_project_permission_owner(project, user, rf):
    request = rf.get("/")
    request.user = user
    perm = IsProjectOwnerOrMember()
    assert perm.has_object_permission(request, None, project)

@pytest.mark.django_db
def test_task_permission_creator(task, user, rf):
    request = rf.put("/")
    request.user = user
    perm = IsTaskOwnerOrAssigned()
    assert perm.has_object_permission(request, None, task)
