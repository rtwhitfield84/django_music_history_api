from django.contrib.auth.models import User
from rest_framework import viewsets
from music_history_api.serializers import *
from music_history_api.models import *

class GenreViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow genres to be viewed or edited
	@rtwhitfield84

	"""

	queryset = genre_model.Genre.objects.all()
	serializer_class = genre_serializer.GenreSerializer