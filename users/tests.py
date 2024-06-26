from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from orders.models import OrderItem
from orders.tests import OrderTestCase


class UsersTestCase(TestCase):
    """
    Тесты для пользователя
    """

    def setUp(self):
        self.valid_email = 'email@test.lemito'
        self.invalid_email = 'wrong_email.test.lemito'

        self.user = User.objects.create_user(username='test', password='ONLYFORTEST', email=self.valid_email)
        self.user.save()

        try:
            self.user2 = User.objects.create_user(username='test2', password='ONLYFORTEST2', email=self.invalid_email)
            self.user2.save()
        except ValidationError as e:
            self.fail(f"Expected ValidationError for invalid email, but got {e}")

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'test')
        self.assertEqual(self.user.email, 'email@test.lemito')
        self.assertEqual(self.user2.username, 'test2')
        self.assertEqual(self.user2.email, 'wrong_email.test.lemito')

        self.assertTrue(self.user.check_password('ONLYFORTEST'))
        self.assertTrue(self.user2.check_password('ONLYFORTEST2'))

        self.assertEqual(self.user.is_staff, False)
        self.assertEqual(self.user.is_superuser, False)

        # self.assertIsNone(User.objects.get(username='test2'))

        # self.assertNotIn(self.invalid_email, User.objects.values_list('email', flat=True))


class ProfileTestCase(TestCase):
    def setUp(self):
        self.order_test_case = OrderTestCase()

        self.valid_email = 'email@test.lemito'
        self.user = User.objects.create_user(username='test', password='ONLYFORTEST', email=self.valid_email)
        self.user.save()

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'test')
        self.assertEqual(self.user.email, 'email@test.lemito')

    def test_profile_creation(self):
        user = authenticate(username='test', password='ONLYFORTEST')

        self.client.force_login(user)
        # self.client.login(username=self.user.username, password=self.user.password)
        response = self.client.get(reverse('user:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.email)

        self.assertContains(response, "Заказы")

    def test_profile_with_order(self):
        user = authenticate(username='test', password='ONLYFORTEST')

        self.client.force_login(user)
        self.order_test_case.setUp()
        order, order_items = self.order_test_case.create_order_with_items()
        self.assertIsNotNone(order)
        self.assertIsNotNone(order_items)

        print("-")
        print(order_items)

        first_item = order_items[0]
        print(first_item)

        response = self.client.get(reverse('user:profile'))

        self.assertContains(response, "Заказы")

        # print(first_item.name)
        # print(response.content)
        # self.assertContains(response, first_item.product.name)

        # self.assertContains(response, order_items.)
