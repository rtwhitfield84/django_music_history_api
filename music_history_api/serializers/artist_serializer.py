from rest_framework import serializers
from music_history_api.models import *


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes Artist model information 
	@rtwhitfield84

	"""


	class Meta:
		model = artist_model.Artist
		fields = ('name', 'year_established', 'label',)