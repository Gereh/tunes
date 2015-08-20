from django.shortcuts import render
from .models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .forms import Login
from django.contrib.auth.hashers import check_password


def home(request):
    slider = Album.objects.all().order_by('publishDate')[:5]
    most_visited = Album.objects.all().order_by('visits')[:12]
    most_downloaded = Album.objects.all().order_by('downloads')[:12]
    advertises = Advertise.objects.filter(position="home").order_by('createdAt')[:1]
    if 'username' not in request.session:
        form = Login()
        username = None
        user = None
    else:
        username = request.session.get('username')
        try :
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            del request.session['username']
            user = None
        form = None
    return render(request, 'home.html', {'slider': slider,
                                         'most_visited': most_visited,
                                         'most_downloaded': most_downloaded,
                                         'advertises': advertises,
                                         'form': form,
                                         'user': user})


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
    try:
        artist = Artist.objects.get(slug=artist_slug)
    except Artist.DoesNotExist:
        raise Http404
    posters = ArtistPoster.objects.filter(artistID=artist.id)
    albums = Album.objects.filter(artistID=artist.id)
    posts = Post.objects.filter(artistID=artist.id)
    return render(requset,'artist.html',{'posters': posters,
                                          'albums': albums,
                                          'artist': artist,
                                          'posts': posts})


def post(request, artist_slug, post_id):
    return render(request,"artist.html")


def login(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return HttpResponse("faild user")
            if check_password(password,user.password):
                request.session['username'] = username
            else:
                return HttpResponse("faild pass")
            return HttpResponseRedirect("/")
    else :
        return HttpResponseRedirect("/")


def logout(requset):
    del requset.session['username']
    return HttpResponseRedirect("/")