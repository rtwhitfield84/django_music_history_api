from django.contrib.auth.models import User
from rest_framework import viewsets
from music_history_api.serializers import *
from music_history_api.models import *

class ArtistViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow artists to be viewed or edited
	@rtwhitfield84

	"""


	queryset = artist_model.Artist.objects.all()
	serializer_class = artist_serializer.ArtistSerializer