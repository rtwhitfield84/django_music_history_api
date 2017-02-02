from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api.models import *


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Album model information 
	@rtwhitfield84

	"""
	user = user_serializer.RestrictedUserSerializer(source='user')


	class Meta:
		model = Album
		fields = ('user','title', 'release_date', 'length', 'artist', 'genre',)