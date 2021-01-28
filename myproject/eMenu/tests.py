from django.test import TestCase
from .models import Card, Dish, CardItems

# Create your tests here.

# models.py
class Card_Dish_and_CardItems_ModelTestCase(TestCase):
    fixtures = ['data.json']

    def setUp(self):
        Card.objects.create(name="Testowa karta", description="Karta utworzona do testow")
        Dish.objects.create(name="Danie testowe", description="Danie utowrzone do testów", price='15')
        card = Card.objects.get(name="Testowa karta")
        dish = Dish.objects.get(name="Danie testowe")
        CardItems.objects.create(card_id = card.id, dish_id = dish.id)