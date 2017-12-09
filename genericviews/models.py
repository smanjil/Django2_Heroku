# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(
            User,
            unique = True,
            on_delete = models.CASCADE
        )
    title = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 300)

    def __str__(self):
        return self.title


