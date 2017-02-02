from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api.models import *
from music_history_api.serializers import user_serializer


class SongSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Song model information 
	@rtwhitfield84

	"""
	user = user_serializer.RestrictedUserSerializer('user')


	class Meta:
		model = song_model.Song
		fields = ('user','title', 'release_date', 'length', 'artist','album', 'genre',)