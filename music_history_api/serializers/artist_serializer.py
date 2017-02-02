from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api.models import *

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Artist model information 
	@rtwhitfield84

	"""
	user = user_serializer.RestrictedUserSerializer(source='user')


	class Meta:
		model = Artist
		fields = ('user','name', 'year_established', 'label',)