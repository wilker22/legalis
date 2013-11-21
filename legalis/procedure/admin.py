# -*- coding: utf-8 -*-

from django.contrib import admin

from legalis.procedure.models import Procedure


class ProcedureModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Procedure, ProcedureModelAdmin)
