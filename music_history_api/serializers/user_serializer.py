from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes user model information 
	@rtwhitfield84

	"""

	class Meta:
		model = User
		fields = '__all__'

class RestrictedUserSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes user model information for restricted users
	@rtwhitfield84

	"""

	class Meta:
		model = User
		fields = ('username', 'first_name')