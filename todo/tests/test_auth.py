import pytest
from todo.tests.conftest import DEFAULT_TEST_USER_PASSWORD
from todo.serializers import RegistrationSerializer
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_register_user(client):
    user = {
        'username': 'JohnDoe',
        'password': 'jd7',
        'email': 'jhon@doe.com'
    }
    response = client.post('/auth/register', user)
    assert response.status_code == 200
    user_object = User.objects.get(username=user['username'])
    expected_data = RegistrationSerializer(user_object).data
    assert response.data['user'] == expected_data

@pytest.mark.django_db
def test_login_user(client, user):
    response = client.post(
        '/auth/login',
        {'username': 'JohnDoe', 'password': DEFAULT_TEST_USER_PASSWORD}
    )
    assert response.status_code == 200

@pytest.mark.django_db
def test_login_user_fails(client, user):
    response = client.post(
        '/auth/login',
        {'username': 'JohnDoe', 'password': 'incorrect_password_2022'}
    )
    assert response.status_code == 401

@pytest.mark.django_db
def test_refresh_token(client, user):
    login_response = client.post(
        '/auth/login',
        {'username': 'JohnDoe', 'password': DEFAULT_TEST_USER_PASSWORD}
    )
    refresh_response = client.post(
        '/auth/refresh-token',
        {'refresh': login_response.data['refresh']}
    )
    assert refresh_response.status_code == 200




# class TestAPIs:
#     pytestmark = [pytest.mark.django_db, pytest.mark.usefixtures("api_client")]

#     def setup_class(self):
#         users = [
#             {'username': 'JohnDoe', 'password': 'jd7', 'email': 'jhon@doe.com'},
#             {'username': 'Blue', 'password': 'blue8', 'email': 'blue@gmail.com'},
#             {'username': 'Bob', 'password': 'bobby1', 'email': 'bob@bob.com'}
#         ]
#         for user in users:
#             User.objects.create_user(
#                 username=user['username'],
#                 password=user['password'],
#                 email=user['email']
#             )

#     def test_user_registration(client):
#         url = reverse('auth/register')
#         response = client.post(
#             url,
#             {
#                 'username': 'User007',
#                 'email': 'user@user.com',
#                 'password': '123'
#             },
#             format='json'
#         )
#         print(response)

#     # def test_todo_list(api_client):
#     #     url = reverse('todo:todo-list')
#     #     response = api_client.get(url)

#     #     logged_user = User.objects.get(username='JohnDoe')
#     #     todo_list = logged_user.todo_list.all()
#     #     expected_data = TODOItemSerializer(todo_list, many=True).data

#     #     assert response.status_code == 200
#     #     assert response.data == expected_data