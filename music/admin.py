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

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

class TrackAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Artist,ArtistAdmin)
admin.site.register(Playlist)
admin.site.register(User)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Track,TrackAdmin)
admin.site.register(Advertise)