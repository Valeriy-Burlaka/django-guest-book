from django.conf.urls import patterns, url

from .views import MessageBoardView


urlpatterns = patterns('',
                       url(r'^$', MessageBoardView.as_view(), name='board'),
                       url(r'(?P<page>\d+)/$', MessageBoardView.as_view(), name='board_page'),
                       )
