from test_plus.test import TestCase

from everycheese.cheeses.models import Cheese
class TestCheese(TestCase):
    def test___str__(self):
        cheese = Cheese.objects.create(
            name='Stracchino',
            description='Semi-sweet cheese that goes well with starches.',
            firmness='soft')
        self.assertEqual(
            cheese.__str__(),'Stracchino')
        
