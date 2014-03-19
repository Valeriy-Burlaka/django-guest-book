from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'guest_book.apps.book.views.index_redirect',
                           name='index_redirect'),
                       url(r'^board/', include('guest_book.apps.book.urls',
                                               namespace='book',
                                               app_name='book')),
                       url(r'^admin/', include(admin.site.urls)),
                      )
