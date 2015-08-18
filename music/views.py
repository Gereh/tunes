from django.shortcuts import render
from .models import *


def home(request):
    slider = Album.objects.all().order_by('publishDate')[:5]
    most_visited = Album.objects.all().order_by('visits')[:12]
    most_downloaded = Album.objects.all().order_by('downloads')[:12]
    advertises = Advertise.objects.filter(position="home").order_by('createdAt')[:1]
    return render(request, 'home.html', {'slider': slider,
                                         'most_visited': most_visited,
                                         'most_downloaded': most_downloaded,
                                         'advertises': advertises})

def album(requset):
    return render(requset,'album.html')