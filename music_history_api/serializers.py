from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Artist, Genre, Album, Song

class UserSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes user model information 
	@rtwhitfield84

	"""

	class Meta:
		model = User
		fields = ('first_name', 'last_name',)


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Artist model information 
	@rtwhitfield84

	"""

	class Meta:
		model = Artist
		fields = ('name', 'year_established', 'label',)


class GenreSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Genre model information 
	@rtwhitfield84

	"""

	class Meta:
		model = Genre
		fields = ('name',)


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Album model information 
	@rtwhitfield84

	"""

	class Meta:
		model = Album
		fields = ('title', 'release_date', 'length', 'artist', 'genre',)


class SongSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Song model information 
	@rtwhitfield84

	"""

	class Meta:
		model = Song
		fields = ('title', 'release_date', 'length', 'artist','album', 'genre',)














