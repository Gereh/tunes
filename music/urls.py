from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^album$', views.album, name='album'),
    url(r'^artist$', views.home, name='home'),
]