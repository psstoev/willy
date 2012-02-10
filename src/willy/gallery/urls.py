from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('gallery.views',

    # Category management:
    url(r'^category/add?', 'add_category'),
    url(r'^category/view/(?P<category_id>\d+)/?', 'view_category'),
    url(r'^category/edit/(?P<category_id>\d+)/?', 'edit_category'),
    url(r'^category/delete/(?P<category_id>\d+)/?', 'delete_category'),
)