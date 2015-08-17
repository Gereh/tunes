from django.shortcuts import render
from .models import *

def home(request):
    slider = Album.objects.all().order_by('publishDate')[:5]
    albums = Album.objects.all()
    albums2 = Album.objects.all()
    return render(request, 'home.html', {'slider': slider, 'albums': albums, 'albums2': albums2})
