from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from cart.models import Cart
from main.models import Products, Addition, Category
import json


class CartTestCase(TestCase):
    """
    Тесты для корзины
    """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.testCategory = Category.objects.create(name='Test Category', slug='test-category')
        self.testProduct = Products.objects.create(name='Test Product With Options', slug='test-product-with-options', price=52.00,
                                                   category=self.testCategory,
                                                   options={"adds": ["сыр:5.00", "бекон:100.00"],
                                                            "Размеры": [{"value": "S", "price": 1},
                                                                        {"value": "M", "price": 1.5}],
                                                            "Тесто": [{"value": "Тонкое", "price": 1},
                                                                      {"value": "Толстое", "price": 1}]})
        # Болванка опций
        empty_options = {}

        self.product = Products.objects.create(name='Test Product', slug='test-product', price=10.00,
                                               category=self.testCategory, options=empty_options)
        self.addition = Addition.objects.create(name='Test Addition', slug='test-addition', price=5.00)

    def test_cart_add_authenticated(self):
        self.client.login(username='testuser', password='12345')

        cart_item = Cart.objects.create(user=self.user, product=self.testProduct, quantity=1, options={"adds": ["сыр:5.00", "бекон:100.00"],
                                                            "Размеры": [{"value": "S", "price": 1},
                                                                        {"value": "M", "price": 1.5}],
                                                            "Тесто": [{"value": "Тонкое", "price": 1},
                                                                      {"value": "Толстое", "price": 1}]})
        response = self.client.post(reverse('cart:cart_remove'), {
                'cart_id': cart_item.id
            })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Cart.objects.filter(id=cart_item.id).exists())

    def test_cart_add_unauthenticated(self):
        cart_item = Cart.objects.create(
                user=self.user,
                product=self.product,
                quantity=1,
                final_price=15.00,
                options='default_option'
            )
        response = self.client.post(reverse('cart:cart_remove'), {
                'cart_id': cart_item.id
            })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Cart.objects.filter(id=cart_item.id).exists())

    # def test_cart_change(self):
    #     cart_item = Cart.objects.create(user=self.user, product=self.testProduct, quantity=1, options={"adds": ["сыр:5.00", "бекон:100.00"],
    #                                                         "Размеры": [{"value": "S", "price": 1},
    #                                                                     {"value": "M", "price": 1.5}],
    #                                                         "Тесто": [{"value": "Тонкое", "price": 1},
    #                                                                   {"value": "Толстое", "price": 1}]})
    #     response = self.client.post(reverse('cart:cart_change'), {
    #         'cart_id': cart_item.id,
    #         'quantity': 2
    #     })
    #     self.assertEqual(response.status_code, 200)
    #     self.assertFalse(Cart.objects.filter(id=cart_item.id).exists())

    def test_cart_remove(self):
        cart_item = Cart.objects.create(user=self.user, product=self.testProduct, quantity=1, options={"adds": ["сыр:5.00", "бекон:100.00"],
                                                            "Размеры": [{"value": "S", "price": 1},
                                                                        {"value": "M", "price": 1.5}],
                                                            "Тесто": [{"value": "Тонкое", "price": 1},
                                                                      {"value": "Толстое", "price": 1}]})
        response = self.client.post(reverse('cart:cart_remove'), {
            'cart_id': cart_item.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Cart.objects.filter(id=cart_item.id).exists())
