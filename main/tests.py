import json

from django.test import TestCase
from django.urls import reverse

from .models import *


class ModelTests(TestCase):
    """
    Класс для проверки модели на работоспособность и всяких "заковырок"
    """

    def setUp(self):
        self.testCategory = Category.objects.create(name='Test Category', slug='test-category')
        self.testProduct = Products.objects.create(name='Test Product', slug='test-product', price=52.00,
                                                   category=self.testCategory,
                                                   options={"adds": ["сыр:5.00", "бекон:100.00"],
                                                            "Размеры": [{"value": "S", "price": 1},
                                                                        {"value": "M", "price": 1.5}],
                                                            "Тесто": [{"value": "Тонкое", "price": 1},
                                                                      {"value": "Толстое", "price": 1}]})
        self.addition = Addition.objects.create(name="Test Addition", slug="test-addition", price=5.00)
        self.special_offer = SpecialOffers.objects.create(name="Test Offer", product=self.testProduct, description="Test Offer")

    def test_category(self):
        self.assertEqual(self.testCategory.name, 'Test Category')
        self.assertEqual(self.testCategory.slug, 'test-category')

    def test_product(self):
        self.assertEqual(self.testProduct.name, 'Test Product')
        self.assertEqual(self.testProduct.slug, 'test-product')
        self.assertEqual(self.testProduct.price, 52.00)
        self.assertEqual(self.testProduct.category, self.testCategory)

        # Проверяем блок опций; он очень сложный, поэтому тестов больше
        self.assertIn("сыр:5.00", self.testProduct.options["adds"])
        self.assertIn("бекон:100.00", self.testProduct.options["adds"])
        self.assertIn({"value": "S", "price": 1}, self.testProduct.options["Размеры"])
        self.assertIn({"value": "M", "price": 1.5}, self.testProduct.options["Размеры"])
        self.assertIn({"value": "Тонкое", "price": 1}, self.testProduct.options["Тесто"])
        self.assertIn({"value": "Толстое", "price": 1}, self.testProduct.options["Тесто"])

    def test_addition(self):
        self.assertEqual(self.addition.name, 'Test Addition')
        self.assertEqual(self.addition.slug, 'test-addition')
        self.assertEqual(self.addition.price, 5.00)

    def test_special_offer(self):
        self.assertEqual(self.special_offer.name, 'Test Offer')
        self.assertEqual(self.special_offer.product, self.testProduct)


class ViewTests(TestCase):
    """
    Класс для проверки вью
    """

    def setUp(self):
        self.testCategory = Category.objects.create(name='Test Category', slug='test-category')
        self.testProduct = Products.objects.create(name='Test Product', slug='test-product', price=52.00,
                                                   category=self.testCategory,
                                                   options={"adds": ["сыр:5.00", "бекон:100.00"],
                                                            "Размеры": [{"value": "S", "price": 1},
                                                                        {"value": "M", "price": 1.5}],
                                                            "Тесто": [{"value": "Тонкое", "price": 1},
                                                                      {"value": "Толстое", "price": 1}]})
        self.addition = Addition.objects.create(name="Test Addition", slug="test-addition", price=5.00)
        self.special_offer = SpecialOffers.objects.create(name="Test Offer", product=self.testProduct, description="Test Offer")

    def test_index_view(self):
        response = self.client.get(reverse('main:index'))
        response_content = self.client.get(reverse('main:index')).content
        response_text = response_content.decode('utf-8')
        print(response_text)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertContains(response, "Test Category")
        # Починить ближе к концу
        self.assertContains(response, "Test Offer")
        # self.assertContains(response, "Test Addition")

    def test_about_view(self):
        response = self.client.get(reverse('main:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about_page.html')

    def test_contacts_view(self):
        response = self.client.get(reverse('main:contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contacts.html')

    import json

    def test_your_view_name_view(self):
        response = self.client.post(reverse('main:your_view_name'), json.dumps({"id": self.testProduct.id}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data, {"data": {"id": self.testProduct.id}, "message": "Пиривет"})

