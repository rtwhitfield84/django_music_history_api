from django.contrib.auth.models import User
from rest_framework import viewsets
from music_history_api.serializers import *
from music_history_api.models import *

class SongViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow songs to be viewed or edited
	@rtwhitfield84

	"""

	queryset = song_model.Song.objects.all()
	serializer_class = song_serializer.SongSerializer