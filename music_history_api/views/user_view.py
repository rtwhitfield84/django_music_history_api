from django.contrib.auth.models import User
from rest_framework import viewsets
from music_history_api.serializers import *
from music_history_api.models import *

class UserViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow users to be viewed or edited
	@rtwhitfield84

	"""
	queryset = User.objects.all()

	def get_serializer_class(self):
		if self.request.user.is_superuser:
			return user_serializer.UserSerializer
		return user_serializer.RestrictedUserSerializer