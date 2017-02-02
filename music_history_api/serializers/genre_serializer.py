from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api.models import *

class GenreSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Genre model information 
	@rtwhitfield84

	"""


	class Meta:
		model = Genre
		fields = ('name',)