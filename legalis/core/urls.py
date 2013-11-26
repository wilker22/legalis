from django.conf.urls import patterns, url

from legalis.core.views import HomepageView

urlpatterns = patterns('',
    url(r'^$', HomepageView.as_view(), name='home'),
)
