from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_create_menu(self):
        title = 'Apple'
        price = 2
        inventory = 50
        item = Menu.objects.create(title=title, price=price, inventory=inventory)

        expected_str = f'{title} : {price}'
        self.assertEqual(str(item), expected_str)
