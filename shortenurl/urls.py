from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'urlapp.views.index', name='urlapp.index'),
    url(r'^!/(?P<short_url_key>\w+)', 'urlapp.views.redirect', name='urlapp.redirect'),

    url(r'^admin/', include(admin.site.urls)),
]
