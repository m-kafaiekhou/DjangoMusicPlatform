from django.contrib import admin

# Local Imports
from .models import *

# Register your models here.


@admin.register(Artist)
class ArtistModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Song)
class SongModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Playlist)
class PlaylistModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    pass
