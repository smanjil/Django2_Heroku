
from __future__ import (
    absolute_import,
    unicode_literals
)
import os
from django.conf import settings
from celery import shared_task
from .models import Product


@shared_task
def add(x, y):
    print ('Sum is: ', x + y)


@shared_task
def clean_media_dir():
    # images name in db
    products = Product.objects.all()
    db_image_name = list(map(lambda item: item.image.url.split('/')[2], products))

    # images name in disk
    disk_image_name = list(map(lambda item: item, os.listdir(settings.MEDIA_ROOT)))

    # find unmatching names from two lists
    unmatching_image_names = list(set(disk_image_name) - set(db_image_name))

    # could not get map to work here
    # map(lambda name: os.remove('/'.join([settings.MEDIA_ROOT, name])), unmatching_image_names)
    for name in unmatching_image_names:
        os.remove('/'.join([settings.MEDIA_ROOT, name]))