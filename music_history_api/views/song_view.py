from django.contrib.auth.models import User
from rest_framework import viewsets
from music_history_api.serializers import *
from music_history_api.models import *

class SongViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow songs to be viewed or edited
	@rtwhitfield84

	"""

	def get_queryset(self):

		"""
		overides the default method to dynamically determine queryset
		returns the songs associated with the current user

		"""

		if self.request.user.is_superuser:
			return song_model.Song.objects.all()
		else:
			return song_model.Song.objects.filter(user=self.request.user)


	serializer_class = song_serializer.SongSerializer