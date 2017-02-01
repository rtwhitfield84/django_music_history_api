from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializes user model information 
	@rtwhitfield84

	"""

	class Meta:
		model = User
		fields = ('first_name', 'last_name',)

