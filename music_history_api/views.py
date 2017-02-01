# from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):

	"""
	API Endpoint to allow users to be viewed or edited
	@rtwhitfield84

	"""

	queryset = User.objects.all()
	serializer_class = UserSerializer
