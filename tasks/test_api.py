import pytest
from django.contrib.auth.models import User
from oauth2_provider.models import get_application_model, AccessToken
from rest_framework.test import APIClient
from django.utils import timezone
from datetime import timedelta
from tasks.models import Task
import pytest

Application = get_application_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def app():
    return Application.objects.create(
        name="TestApp",
        client_type="confidential",
        authorization_grant_type="password"
    )


@pytest.fixture
def user1(db):
    return User.objects.create_user(username="user1", password="pass123")


@pytest.fixture
def user2(db):
    return User.objects.create_user(username="user2", password="pass123")


@pytest.fixture
def token_user1(user1, app):
    return AccessToken.objects.create(
        user=user1,
        token='token-user1',
        application=app,
        expires=timezone.now() + timedelta(days=1),
        scope='read write'
    )


@pytest.fixture
def token_user2(user2, app):
    return AccessToken.objects.create(
        user=user2,
        token='token-user2',
        application=app,
        expires=timezone.now() + timedelta(days=1),
        scope='read write'
    )

@pytest.mark.django_db
def test_register_user(api_client):
    response = api_client.post("/api/register/", {
        "username": "nuevo",
        "password": "clave123456",
        "email": "correo@ejemplo.com"
    })
    assert response.status_code == 201


def test_create_task(api_client, token_user1):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer token-user1')
    response = api_client.post("/api/tasks/", {
        "title": "Nueva tarea",
        "description": "Descripción"
    }, format='json')
    assert response.status_code == 201
    assert Task.objects.count() == 1


def test_list_tasks(api_client, token_user1):
    Task.objects.create(user=token_user1.user, title="Tarea 1", description="...")
    api_client.credentials(HTTP_AUTHORIZATION='Bearer token-user1')
    response = api_client.get("/api/tasks/")
    assert response.status_code == 200
    assert len(response.data) == 1


def test_user_cannot_see_others_tasks(api_client, token_user1, token_user2):
    Task.objects.create(user=token_user1.user, title="Privada", description="No accesible")
    api_client.credentials(HTTP_AUTHORIZATION='Bearer token-user2')
    response = api_client.get("/api/tasks/")
    assert response.status_code == 200
    assert len(response.data) == 0

@pytest.mark.django_db
def test_invalid_token(api_client):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer token-no-valido')
    response = api_client.get("/api/tasks/")
    assert response.status_code == 401
