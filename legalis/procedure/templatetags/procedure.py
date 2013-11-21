# -*- coding: utf-8 -*-

from django import template

from legalis.procedure.models import Procedure


register = template.Library()


@register.simple_tag
def procedure_list(template_name="procedure/procedure_list.html"):
    """
    Template Tag que renderiza a lista de atuacoes

    Formas de usar::

        {% procedure_list template_name='my_template.html' %}
        {% procedure_list %}

    """
    # Pesquisando as atuacoes
    procedures = Procedure.objects.all()

    t = template.loader.get_template(template_name)
    render = t.render(template.Context({'object_list': procedures}))
    return render
