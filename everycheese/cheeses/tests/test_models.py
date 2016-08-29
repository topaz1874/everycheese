from test_plus.test import TestCase

from ..factories import CheeseFactory
from everycheese.cheeses.models import Cheese

class TestCheese(TestCase):
    def test___str__(self):
        cheese = CheeseFactory(name='Stracchino')
        # cheese = Cheese.objects.create(
        #     name='Stracchino',
        #     description='Semi-sweet cheese that goes well with starches.',
        #     firmness='soft')
        self.assertEqual(
            cheese.__str__(),'Stracchino')

    def test_simple_creation(self):
        self.assertEqual(0, Cheese.objects.count())
        for _ in range(10):
            CheeseFactory()
        self.assertEqual(10, Cheese.objects.count())
        
