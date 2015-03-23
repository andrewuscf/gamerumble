from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples
    # url(r'^$', 'LeagueSports.views.home', name='home'),
    # url(r'^LeagueSports/', include('LeagueSports.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'', include('drafter.urls')),
    url(r'explore/', include('explorer.urls')),
    url(r'', include('drafter.api.urls')),
)
