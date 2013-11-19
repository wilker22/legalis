# -*- coding: utf-8 -*-

from django.views.generic.list import ListView

from legalis.models import Operation


class OperationListView(ListView):
    template_name = "operations/operations_list.html"
    model = Operation
