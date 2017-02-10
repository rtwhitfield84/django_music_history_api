from rest_framework import serializers
from music_history_api.models import *
from music_history_api.serializers import artist_serializer, genre_serializer


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Album model information 
	@rtwhitfield84

	"""
	artist = artist_serializer.ArtistSerializer('artist',read_only=True)
	genre = genre_serializer.GenreSerializer('genre',read_only=True)


	class Meta:
		model = album_model.Album
		fields = ('title', 'release_date', 'length', 'artist', 'genre',)