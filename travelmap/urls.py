from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'logbook.views.home', name='home'),
    url(r'^map/$', 'logbook.views.map', name='map'),
    url(r'^journeys/$', 'logbook.views.my_journeys', name='my_journeys'),
    url(r'^journeys/add/$', 'logbook.views.add_journey', name='add_journey'),
    url(r'^journeys/(?P<journey_id>\w+)/$', 'logbook.views.view_journey', name='view_journey'),
    url(r'^journeys/(?P<journey_id>\w+)/edit/$', 'logbook.views.edit_journey', name='edit_journey'),
    url(r'^journeys/(?P<journey_id>\w+)/remove/$', 'logbook.views.remove_journey', name='remove_journey'),
    # User registration
    url(r'^register/$', 'logbook.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)