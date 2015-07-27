from django.contrib import admin
from .models import Playlist, Album, Track, Artist, User



class TrackInline(admin.StackedInline):
    model = Track
    extra = 0



class AlbumAdmin(admin.ModelAdmin):
    inlines = [TrackInline]



admin.site.register(Artist)
admin.site.register(Playlist)
admin.site.register(User)
admin.site.register(Album,AlbumAdmin)
