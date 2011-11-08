from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
from mysite import settings

urlpatterns = patterns('',
    (r'^pair/?$', 'pair.views.index'),
    (r'^pair/get_pair_table/?$', 'pair.views.get_pair_table'),
    (r'^pair/do_pair/(?P<programmer_0_id>.+?)/(?P<programmer_1_id>.+?)/?$', 'pair.views.do_pair'),
    (r'^pair/programmer/?$', 'pair.views.new_programmer'),
    (r'^pair/programmer/(?P<programmer_id>.+?)/?$', 'pair.views.process_programmer'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    
)
