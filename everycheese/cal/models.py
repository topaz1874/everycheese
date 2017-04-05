from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CalItem(models.Model):
    uploadfile = models.FileField(upload_to='uploads/%Y/%m/%d/')