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

    # Login/logout:
    url(r'^login/?', 'django.contrib.auth.views.login', {'template_name' : 'login.html'}),
    url(r'^logout/?', 'django.contrib.auth.views.logout_then_login', {'login_url' : '/login/'}),

    # Welcome screen:
    url(r'^welcome/?', 'views.welcome'),

    # Registration:
    url(r'^register/?', 'views.register'),

    # Gallery urls:
    url(r'^gallery/?', include('gallery.urls')),
)
