from django.contrib import admin
from music_history_api.models import Artist, Genre, Album, Song


admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Song)