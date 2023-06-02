
from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title='Apple', price=2, inventory=50)
        self.menu2 = Menu.objects.create(title='Banana', price=3, inventory=40)



    def test_getall(self):
        menus = Menu.objects.all()
        self.assertEqual(len(menus), 2)
        self.assertIn(self.menu1, menus)
        self.assertIn(self.menu2, menus)

