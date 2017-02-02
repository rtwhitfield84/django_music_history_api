from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api.models import *
from music_history_api.serializers import user_serializer

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Artist model information 
	@rtwhitfield84

	"""
	user = user_serializer.RestrictedUserSerializer('user')


	class Meta:
		model = artist_model.Artist
		fields = ('user','name', 'year_established', 'label',)