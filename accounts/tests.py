from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model
from .forms import UserSignUpForm
# Create your tests here.


class MyViewTestCase(TestCase):
    def test_signup(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


User = get_user_model()

class UserSignUpFormTestCase(TestCase):
    def test_save_method(self):
        form_data = {
            'username': 'testuser',
            'password1': 'NotEasyPassword124^',
            'password2': 'NotEasyPassword124^',
            'email': 'testuser@example.com',
        }
        form = UserSignUpForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.is_user)


# class CreateUserTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.url = reverse('signup')
#         self.user_data = {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'password'}

    # def test_create_user(self):
    #     response = self.client.post(self.url, self.user_data)
    #     print(self.user_data)
    #     self.assertEqual(response.status_code, 200)
    #     count =RegularUser.objects.count()
    #     self.assertNotEqual(count, 0 , "User was created")
    #     self.assertTrue(RegularUser.objects.filter(username='testuser').exists())
