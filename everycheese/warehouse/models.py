#-*-coding:utf-8 -*-

from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import iri_to_uri
from django.utils.http import urlquote

from autoslug import AutoSlugField

# Create your models here.

class WarehouseItem(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=True, populate_from="name")
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('warehouse:detail', kwargs={'slug': self.slug})


class TransQuerySet(models.QuerySet):
    def trans_in(self):
        return self.filter(trans_amount__gte=0)

    def trans_out(self):
        return self.filter(trans_amount__lt=0)


class TransManager(models.Manager):
    def get_queryset(self):
        return TransQuerySet(self.model, using=self._db)
    def get_trans_in(self):
        return self.get_queryset().trans_in()
    def get_trans_out(self):
        return self.get_queryset().trans_out()


class Trans(models.Model):
    CHOICES = (
        (u'伍嘉煦', u'伍嘉煦'),
        (u'吴建涛', u'吴建涛'))

    trans_date = models.DateField("入库时间",auto_now=False, auto_now_add=False)
    item = models.ForeignKey(WarehouseItem)
    trans_amount = models.DecimalField(max_digits=7, decimal_places=2)
    trans_man = models.CharField("经手人",choices=CHOICES,max_length=255)

    objects = TransManager()

    def __unicode__(self):
        return '%s - %s'  % (self.item.name, str(self.trans_date))
    
    # def get_absolute_url(self):
    #     return iri_to_uri('/warehouse/%s' % urlquote(self.item.slug))
    #     # return reverse('warehouse:detail', kwargs={'slug': self.item.slug})