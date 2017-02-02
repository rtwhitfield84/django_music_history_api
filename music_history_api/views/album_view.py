from django.contrib.auth.models import User
from rest_framework import viewsets
from music_history_api.serializers import *
from music_history_api.models import *

class AlbumViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow albums to be viewed or edited
	@rtwhitfield84

	"""

	def get_queryset(self):

		"""
		overides the default method to dynamically determine queryset
		returns the albums associated with the current user

		"""

		if self.request.user.is_superuser:
			return album_model.Album.objects.all()
		else:
			return album_model.Album.objects.filter(user=self.request.user)


	serializer_class = album_serializer.AlbumSerializer