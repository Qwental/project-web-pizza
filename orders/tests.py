from django.test import TestCase

from django.contrib.auth.models import User

from cart.models import Cart
from main.models import Products, Category
from orders.models import Order, OrderItem


class OrderTestCase(TestCase):
    """
    Тесты для корзины
    """

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.testCategory = Category.objects.create(name='Test Category', slug='test-category')
        self.testProduct = Products.objects.create(name='Test Product With Options', slug='test-product-with-options',
                                                   price=52.00,
                                                   category=self.testCategory,
                                                   options={"adds": ["сыр:5.00", "бекон:100.00"],
                                                            "Размеры": [{"value": "S", "price": 1},
                                                                        {"value": "M", "price": 1.5}],
                                                            "Тесто": [{"value": "Тонкое", "price": 1},
                                                                      {"value": "Толстое", "price": 1}]})
        self.testProduct2 = Products.objects.create(name='Test Product With Options2',
                                                    slug='test-product-with-options2', price=52342.00,
                                                    category=self.testCategory,
                                                    options={"adds": ["сыр:5.00"],
                                                             "Размеры": [{"value": "S", "price": 1},
                                                                         {"value": "M", "price": 1.5}],
                                                             "Тесто": [{"value": "Тонкое", "price": 1},
                                                                       {"value": "Толстое", "price": 1}]})

        self.cart_item1 = Cart.objects.create(user=self.user, product=self.testProduct, quantity=1,
                                              options={"adds": ["сыр:5.00", "бекон:100.00"],
                                                       "Размеры": [{"value": "S", "price": 1},
                                                                   {"value": "M", "price": 1.5}],
                                                       "Тесто": [{"value": "Тонкое", "price": 1},
                                                                 {"value": "Толстое", "price": 1}]})
        self.cart_item2 = Cart.objects.create(user=self.user, product=self.testProduct2, quantity=1,
                                              options={"adds": ["сыр:5.00"],
                                                       "Размеры": [{"value": "S", "price": 1},
                                                                   {"value": "M", "price": 1.5}],
                                                       "Тесто": [{"value": "Тонкое", "price": 1},
                                                                 {"value": "Толстое", "price": 1}]})

    def create_order(self):
        order = Order.objects.create(
            user=self.user,
            requires_delivery=True,
            delivery_address="qwert",
            payment_on_get=True,
        )

        for cart_item in [self.cart_item1, self.cart_item2]:
            product = cart_item.product
            name = cart_item.product.name
            price = cart_item.final_price
            quantity = cart_item.quantity

            options = cart_item.options

            OrderItem.objects.create(
                order=order,
                product=product,
                name=name,
                price=price,
                quantity=quantity,
                options=options,
            )
            product.save()

        return order

    def test_create_order_with_items(self):
        order = self.create_order()

        self.assertIsNotNone(order)

        order_items = OrderItem.objects.filter(order=order)

        print(order_items)

        self.assertEqual(len(order_items), 2)

        first_item = order_items[0]
        self.assertEqual(first_item.product, self.testProduct)
        self.assertEqual(first_item.quantity, 1)
        self.assertEqual(first_item.options, self.cart_item1.options)

        second_item = order_items[1]
        self.assertEqual(second_item.product, self.testProduct2)
        self.assertEqual(second_item.quantity, 1)
        self.assertEqual(second_item.options, self.cart_item2.options)