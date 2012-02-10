from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    # Login/logout:
    url(r'^login/?', 'django.contrib.auth.views.login', {'template_name' : 'login.html'}),
    url(r'^logout/?', 'django.contrib.auth.views.logout_then_login'),

    # Welcome screen:
    url(r'^welcome/?', 'session.views.welcome'),

    # Registration:
    url(r'^register/?', 'session.views.register'),

    # Profile editing:
    url(r'^profile/edit/?', 'session.views.edit_profile'),

)
