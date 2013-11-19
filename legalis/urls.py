from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^atuacoes/$', 'legalis.views.operations_list', name='operations_list'),
)
