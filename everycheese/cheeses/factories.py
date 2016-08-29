import factory
import factory.fuzzy

from .models import Cheese

class CheeseFactory(factory.django.DjangoModelFactory):

    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: obj.name)

    class Meta:
        model = Cheese

