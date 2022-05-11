import pytest
from datetime import date
from todo.models import TODOItem
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

DEFAULT_TEST_USER_PASSWORD = 'ilovejanedoe'

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def auth_client(user, client):
    response = client.post(
        '/auth/login',
        {'username': user.username, 'password': DEFAULT_TEST_USER_PASSWORD}
    )
    auth_token = response.data['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {auth_token}')
    return client

@pytest.fixture
def user():
    return User.objects.create_user(
        username='JohnDoe',
        email='john.doe@gmail.com',
        password=DEFAULT_TEST_USER_PASSWORD
    )

@pytest.fixture
def todo_item(user):
    mock_image = SimpleUploadedFile(
        name='test_image.jpg',
        content=b'mock',
        content_type='image/jpeg'
    )
    return TODOItem.objects.create(
        owner=user,
        title='Work',
        description='Need to do some stuff...',
        image=mock_image,
        deadline=date.today().strftime('%Y-%m-%d')
    )