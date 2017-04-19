from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('^!/(?P<short_url_key>\w+)', 'urlapp.views.redirect', name='urlapp.redirect'),

    url(r'^admin/', include(admin.site.urls)),
]
