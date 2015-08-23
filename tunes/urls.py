"""tunes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from music import views
from django.conf.urls.static import static

urlpatterns = [
    # home
    url(r'^$', views.home, name='home'),
    # admin
    url(r'^admin/', include(admin.site.urls)),
    # music
    url(r'^music/', include('music.urls')),
    # media
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # captcha
    url(r'^captcha/', include('captcha.urls')),
    # login
    url(r'^login/$', views.login, name='login'),
    # logout
    url(r'^logout/$', views.logout, name='logout'),
    #profile
    url(r'^profile/$', views.profile, name='profile'),
    # register
    url(r'^register/$', views.register, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
