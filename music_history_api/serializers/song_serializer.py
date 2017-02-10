from rest_framework import serializers
from music_history_api.models import *
from music_history_api.serializers import artist_serializer, genre_serializer, album_serializer


class SongSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Song model information 
	@rtwhitfield84

	"""
	artist = artist_serializer.ArtistSerializer('artist')
	genre = genre_serializer.GenreSerializer('genre')
	album = album_serializer.AlbumSerializer('album')


	class Meta:
		model = song_model.Song
		fields = ('title', 'release_date', 'length', 'artist','album', 'genre',)
