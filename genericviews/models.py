# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 300)

    def __str__(self):
        return self.title


