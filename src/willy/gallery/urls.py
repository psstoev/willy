from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('gallery.views',

    # Category management:
    url(r'^category/add?', 'add_category'),
    url(r'^category/view/(?P<category_id>\d+)/?', 'view_category'),
    url(r'^category/edit/(?P<category_id>\d+)/?', 'edit_category'),
    url(r'^category/delete/(?P<category_id>\d+)/?', 'delete_category'),
    
    # Picture management:
    url(r'^picture/upload/?', 'upload_picture'),
    url(r'^picture/view/(?P<picture_id>\d+)/?', 'view_picture'),
    url(r'^picture/edit/(?P<picture_id>\d+)/?', 'edit_picture'),
    url(r'^picture/delete/(?P<picture_id>\d+)/?', 'delete_picture'),
    
    # Menu URLs
    url(r'^pictures/?$', 'view_pictures'),
    url(r'^categories/?$', 'view_categories'),  
)
