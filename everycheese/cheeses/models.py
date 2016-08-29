from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django_countries.fields import CountryField

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

@python_2_unicode_compatible
class Cheese(TimeStampedModel):

    FIRMNESS_CHOICES = (
        #(actual_value, huamam_readable_value)
        ('unspecified', 'Unspecified'),
        ('soft', 'Soft'),
        ('semi-soft', 'Semi-Soft'),
        ('semi-hard', 'Semi-Hard'),
        ('hard','Hard'),
    )

    # created
    # modified
    name = models.CharField("Name of Cheese", max_length=255)
    slug = AutoSlugField("Cheese Address",
        unique=True, always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True)
    firmness = models.CharField("Firmness", max_length=20,
        choices=FIRMNESS_CHOICES, default='unspecified')
    country_of_origin = CountryField("Country of Origin", null=True, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cheeses:detail', kwargs={'slug': self.slug})