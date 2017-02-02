from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api.models import *

class SongSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Song model information 
	@rtwhitfield84

	"""
	user = user_serializer.RestrictedUserSerializer(source='user')


	class Meta:
		model = Song
		fields = ('user','title', 'release_date', 'length', 'artist','album', 'genre',)