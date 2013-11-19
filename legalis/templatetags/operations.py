# -*- coding: utf-8 -*-

from django import template

from legalis.models import Operation


register = template.Library()


@register.simple_tag
def operation_list(template_name="operations/operations_list.html"):
    """
    Template Tag que renderiza a lista de atuacoes

    Formas de usar::

        {% operation_list template_name='my_template.html' %}
        {% operation_list %}

    """
    # Pesquisando as atuacoes
    operations = Operation.objects.all()

    t = template.loader.get_template(template_name)
    render = t.render(template.Context({'object_list': operations}))
    return render
