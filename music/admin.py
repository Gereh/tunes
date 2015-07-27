from django.contrib import admin
from .models import Playlist, Album, Track, Artist, User


class AlbumInline(admin.StackedInline):
    model = Album
    extra = 0


class TrackInline(admin.StackedInline):
    model = Track
    extra = 0


class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumInline, TrackInline]

class AlbumAdmin(admin.ModelAdmin):
    inlines = [TrackInline]



admin.site.register(Artist, ArtistAdmin)
admin.site.register(Playlist)
admin.site.register(User)
admin.site.register(Album,AlbumAdmin)
