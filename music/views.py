from django.shortcuts import render
from .models import *

def home(request):
    slider = Album.objects.all().order_by('publishDate')[:5]
    return render(request, 'home.html', {'slider': slider})
