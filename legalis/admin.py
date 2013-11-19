# -*- coding: utf-8 -*-

from django.contrib import admin

from legalis.models import Operation


class OperationModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Operation, OperationModelAdmin)
