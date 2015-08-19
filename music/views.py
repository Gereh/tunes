from django.shortcuts import render
from .models import *
from django.http import Http404


def home(request):
    slider = Album.objects.all().order_by('publishDate')[:5]
    most_visited = Album.objects.all().order_by('visits')[:12]
    most_downloaded = Album.objects.all().order_by('downloads')[:12]
    advertises = Advertise.objects.filter(position="home").order_by('createdAt')[:1]
    return render(request, 'home.html', {'slider': slider,
                                         'most_visited': most_visited,
                                         'most_downloaded': most_downloaded,
                                         'advertises': advertises})


def album(requset, album_slug):
    try:
        album = Album.objects.get(slug=album_slug)
    except Album.DoesNotExist:
        raise Http404
    album_covers = AlbumCover.objects.filter(albumID=album.id)
    tracks = Track.objects.filter(albumID=album.id)
    return render(requset,'album.html', {'album': album,
                                         'album_covers': album_covers,
                                         'tracks': tracks})


def artist(requset, artist_slug):
    return render(requset,'artist.html')