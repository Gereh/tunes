#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .forms import Login, ForgotPass, Register
from django.contrib.auth.hashers import check_password
from django.forms.util import ErrorList


# description : this function will check that user logined or no,if logined it will return {'user' : obj,'form' : None}
# else will return {'user' : None,'form' : obj}

# params : request object for retrive sessions

# return : a dic that indicate result
def user_auth(request):
    res = {}
    # checking that user logined or no
    if 'username' not in request.session:
        form = Login()
        username = None
        res['user'] = None
        res['form'] = form
        res['is_authenticated'] = False
    # mean that user is not login
    else:
        # retrieving user name form session
        username = request.session.get('username')
        try:
            # retrieving user form session
            user = User.objects.get(username=username)
            res['user'] = user
            res['form'] = None
            res['is_authenticated'] = True
        except User.DoesNotExist:
            del request.session['username']
            res['user'] = None
            res['form'] = Login()
            res['is_authenticated'] = False
    return res


# Responsible for handling "/" url
def home(request):
    # retrieving data from data base
    slider = Album.objects.all().order_by('publishDate')[:5]
    most_visited = Album.objects.all().order_by('visits')[:12]
    most_downloaded = Album.objects.all().order_by('downloads')[:12]
    advertises = Advertise.objects.filter(position="home").order_by('createdAt')[:1]

    # receiving user or form to fill user data
    user_login = user_auth(request)

    # creating data for rendering page
    rendering_data = {'slider': slider,
                      'most_visited': most_visited,
                      'most_downloaded': most_downloaded,
                      'advertises': advertises,
                      'form': user_login['form'],
                      'user': user_login['user']}

    # checking that user entered incorrect pass and providing result
    if 'incorrect_pass' in request.COOKIES.keys():
        rendering_data['print_incorrect_pass'] = True
        res = render(request, 'home.html', rendering_data)
        res.delete_cookie('incorrect_pass')
    else:
        rendering_data['print_incorrect_pass'] = False
        res = render(request, 'home.html', rendering_data)

    # returning result
    return res


# Responsible for handling "/music/album/(albumname)/" url
def album(request, album_slug):
    # retrieving objects from database and handling related error
    try:
        album = Album.objects.get(slug=album_slug)
    except Album.DoesNotExist:
        raise Http404
    album_covers = AlbumCover.objects.filter(albumID=album.id)
    tracks = Track.objects.filter(albumID=album.id)

    # receiving user or form to fill user data
    user_login = user_auth(request)

    # providing data for rendering
    rendering_data = {'album': album,
                      'album_covers': album_covers,
                      'tracks': tracks,
                      'form': user_login['form'],
                      'user': user_login['user']}

    # checking that user entered incorrect pass and providing result
    if 'incorrect_pass' in request.COOKIES.keys():
        rendering_data['print_incorrect_pass'] = True
        res = render(request, 'album.html', rendering_data)
        res.delete_cookie('incorrect_pass')
    else:
        rendering_data['print_incorrect_pass'] = False
        res = render(request, 'album.html', rendering_data)

    # returning result
    return res


# Responsible for handling "/music/artist/(albumname)/" url
def artist(request, artist_slug):
    # retrieving objects from database and handling related error
    try:
        artist = Artist.objects.get(slug=artist_slug)
    except Artist.DoesNotExist:
        raise Http404
    posters = ArtistPoster.objects.filter(artistID=artist.id)
    albums = Album.objects.filter(artistID=artist.id)
    posts = Post.objects.filter(artistID=artist.id)

    # receiving user or form to fill user data
    user_login = user_auth(request)

    # providing data for rendering
    rendering_data = {'posters': posters,
                       'albums': albums,
                       'artist': artist,
                       'posts': posts,
                       'form': user_login['form'],
                       'user': user_login['user']}

    # checking that user entered incorrect pass and providing result
    if 'incorrect_pass' in request.COOKIES.keys():
        rendering_data['print_incorrect_pass'] = True
        res = render(request, 'artist.html', rendering_data)
        res.delete_cookie('incorrect_pass')
    else:
        rendering_data['print_incorrect_pass'] = False
        res = render(request, 'artist.html', rendering_data)

    # returning result
    return render(request, 'artist.html', rendering_data)


def post(request, artist_slug, post_id):
    return render(request, "artist.html")


# Responsible for handling "/login/" url
def login(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                res = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                res.set_cookie('incorrect_pass', 1)
                return res
            if check_password(password, user.password):
                request.session['username'] = username
            else:
                res = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                res.set_cookie('incorrect_pass', 1)
                return res
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            res = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            res.set_cookie('incorrect_pass', 1)
            return res
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# Responsible for handling "/logout/" url
def logout(request):
    if 'username' in request.session.keys():
        del request.session['username']
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# Responsible for handling "/register/" url
def register(request):
    if request.method == 'POST':
        register_form = Register(request.POST)
        if register_form.is_valid():
            password1 = register_form.cleaned_data['password']
            password2 = register_form.cleaned_data['password2']
            if password1 == password2:
                try:
                    new_user = User()
                    new_user.username = register_form.cleaned_data['username']
                    new_user.email = register_form.cleaned_data['email']
                    new_user.name = register_form.cleaned_data['name']
                    new_user.password = password1
                    new_user.save()
                    HttpResponseRedirect('/')  # need attention
                    # message = '????? ???????? ????? ??'
                    message = '???? ?????? ??? ????? ?? ???? ???? ????.'
                except Exception as e:
                    return HttpResponse("user creation faild - " + str(e))
            else:
                pass
        else:
            login_form = Login()  # need attention
            forgotPass_form = ForgotPass()  # need atention
    else:
        register_form = Register()
        forgotPass_form = ForgotPass()
        login_form = Login()
    return render(request, "register.html", {'register_form': register_form,
                                             'forgotPass_form': forgotPass_form,
                                             'login_form': login_form})


def profile(request):
    return render(request, "profile.html")
