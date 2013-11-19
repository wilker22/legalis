from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'', include('legalis.urls')),
)

# Django flatpages
urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^pages/(?P<url>.*)$', 'flatpage', name='flatpages'),
)
