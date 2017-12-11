# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from genericviews.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # item in table
    list_display = ('capitalized_title', 'desc', 'upper_user')

    # show col values in preformatted way
    def capitalized_title(self, obj):
        return ("%s" % obj.title).title()
    capitalized_title.short_description = 'title'

    def upper_user(self, obj):
        return ("%s" % obj.user).upper()
    upper_user.short_description = 'user'

    # register fields for filter to appear in side
    list_filter = ('user',)

    # max no of items to show in a page
    list_per_page = 5

    # sorting items in column
    ordering = ['title']

    # search fields
    search_fields = ['title']