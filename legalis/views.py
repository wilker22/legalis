# -*- coding: utf-8 -*-

from django.shortcuts import render


def operations_list(request):
    return render(request, "operations/operations_list.html")
