import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    resp = client.post(
        "/users/",
        {"username": "newuser", "password": "pass1234"},
    )
    assert resp.status_code == 201
    assert "password" not in resp.data

@pytest.mark.django_db
def test_user_me(user):
    client = APIClient()
    client.force_authenticate(user=user)
    resp = client.get("/users/me/")
    assert resp.status_code == 200
    assert resp.data["username"] == user.username
