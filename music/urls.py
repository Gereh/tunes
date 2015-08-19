from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^album/(?P<album_slug>[\w-]+)/$', views.album, name='album'),
    url(r'^artist/(?P<artist_slug>[\w-]+)/$', views.artist, name='artist'),
    url(r'^artist/(?P<artist_slug>[\w-]+)/post/(?P<post_id>[0-9]+)/$', views.post, name='post'),
]