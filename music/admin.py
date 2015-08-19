from django.contrib import admin
from .models import *



class TrackInline(admin.StackedInline):
    model = Track
    extra = 0


class AlbumCoverInline(admin.StackedInline):
    model = AlbumCover
    extra = 0


class AlbumAdmin(admin.ModelAdmin):
    inlines = [TrackInline, AlbumCoverInline]
    list_display = ('id', 'name',)

class ArtistPosterAdmin(admin.StackedInline):
    model = ArtistPoster
    extra = 3

class ArtistPostAdmin(admin.StackedInline):
    model = Post
    extra = 1

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    inlines = [ArtistPosterAdmin,ArtistPostAdmin]

class TrackAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Artist,ArtistAdmin)
admin.site.register(Playlist)
admin.site.register(User)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Track,TrackAdmin)
admin.site.register(Advertise)