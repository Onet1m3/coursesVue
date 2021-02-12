from rest_framework.test import APITestCase
from app.users.models import User
from app.users.serializers import RegisterSerializer


class AuthAPITestCase(APITestCase):
    """Тесты для регистрации пользователя:
    проверка эндпоинта, сериализатора и представления
    """

    def setUp(self):
        self.user1 = User.objects.create(first_name="Alex", email="test1@test.ru", password="q1w2e3r4t5")
        self.uri_register = '/auth/register/'
        self.uri_login = '/auth/token/'

    def test_registration(self):
        data = {
            'first_name': 'Tom',
            'email': 'test@gmail.ru',
            'password': 'qwerty21'
        }
        response = self.client.post(self.uri_register, data=data)
        self.assertEqual(response.status_code, 201)

        data.pop('password')
        self.assertEqual(response.data, data)

        data = {
            'first_name': 'Alex', 
            'email': 'test1@test.ru', 
            'password': 'q1w2e3r4t5'
        }
        response = self.client.post(self.uri_register, data=data)
        self.assertEqual(response.status_code, 400)
        
       

