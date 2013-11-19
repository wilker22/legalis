from django.conf.urls import patterns, url

from legalis.views import OperationListView

urlpatterns = patterns('',
    url(r'^atuacoes/$', OperationListView.as_view(), name='operations_list'),
)
