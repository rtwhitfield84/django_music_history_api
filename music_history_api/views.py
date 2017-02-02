# from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, ArtistSerializer,GenreSerializer,AlbumSerializer,SongSerializer,RestrictedUserSerializer
from .models import Artist, Genre, Album, Song

class UserViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow users to be viewed or edited
	@rtwhitfield84

	"""
	queryset = User.objects.all()

	def get_serializer_class(self):
		if self.request.user.is_superuser:
			return UserSerializer
		return RestrictedUserSerializer

class ArtistViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow artists to be viewed or edited
	@rtwhitfield84

	"""
	
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer

class GenreViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow genres to be viewed or edited
	@rtwhitfield84

	"""

	queryset = Genre.objects.all()
	serializer_class = GenreSerializer

class AlbumViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow albums to be viewed or edited
	@rtwhitfield84

	"""

	queryset = Album.objects.all()
	serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow songs to be viewed or edited
	@rtwhitfield84

	"""

	queryset = Song.objects.all()
	serializer_class = SongSerializer

