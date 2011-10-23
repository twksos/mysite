from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
from mysite import settings

urlpatterns = patterns('',
    (r'^pair/$', 'pair.views.index'),
    (r'^pair/get_pair_table$', 'pair.views.get_pair_table'),
    (r'^pair/init$', 'pair.views.prepare_data'),
    (r'^pair/do_pair/(?P<programmer_0_id>.+?)/(?P<programmer_1_id>.+?)/$', 'pair.views.do_pair'),
    (r'^pair/new_programmer/(?P<programmer_name>.+?)/$', 'pair.views.new_programmer'),
    (r'^pair/delete_programmer/(?P<programmer_id>.+?)/$', 'pair.views.delete_programmer'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
)
