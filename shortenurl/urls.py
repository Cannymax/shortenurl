from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'shortenurl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^!/(?P<short_url_key>\w+)', 'urlapp.views.redirect', name='urlapp.redirect'),

    # url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
]
