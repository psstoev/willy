from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'willy.views.home', name='home'),
    # url(r'^willy/', include('willy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Session urls:
    url(r'^session/?', include('session.urls')),

    # Gallery urls:
    url(r'^gallery/?', include('gallery.urls')),

    # Index page:
    url(r'^$', include('session.urls')),
)
