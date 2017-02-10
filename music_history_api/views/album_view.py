from rest_framework import viewsets
from music_history_api.serializers import *
from music_history_api.models import *

class AlbumViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow albums to be viewed or edited
	@rtwhitfield84

	"""

	queryset = album_model.Album.objects.all()
	serializer_class = album_serializer.AlbumSerializer