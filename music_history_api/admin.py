from django.contrib import admin
from music_history_api.models import *


admin.site.register(artist_model.Artist)
admin.site.register(genre_model.Genre)
admin.site.register(album_model.Album)
admin.site.register(song_model.Song)



