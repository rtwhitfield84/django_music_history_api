from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api.models import *
from music_history_api.serializers import user_serializer, artist_serializer, genre_serializer


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Album model information 
	@rtwhitfield84

	"""
	user = user_serializer.RestrictedUserSerializer('user')
	artist = artist_serializer.ArtistSerializer('artist')
	genre = genre_serializer.GenreSerializer('genre')


	class Meta:
		model = album_model.Album
		fields = ('user','title', 'release_date', 'length', 'artist', 'genre',)