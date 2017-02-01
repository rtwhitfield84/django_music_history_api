from django.contrib.auth.models import User
from django.db import models

class Artist(models.Model):
	"""
	Artist model maintains the information realted to an artist
	@rtwhitfield84

	"""

	name = models.CharField(max_length=128)
	year_established = models.CharField(max_length=4, blank=True)
	label = models.CharField(max_length=128, blank=True)

	class Meta:
		verbose_name_plural = "Artist's"

	def __str__(self):
		return '{}'.format(self.name)

class Genre(models.Model):
	"""
	genre model maintains the information realted to a genre
	@rtwhitfield84

	"""

	name = models.CharField(max_length=128, blank=True)

	class Meta:
		verbose_name_plural = "Genre's"

	def __str__(self):
		return '{}'.format(self.name)

class Album(models.Model):
	"""
	Album model maintains the information realted to an album
	@rtwhitfield84

	"""

	title = models.CharField(max_length=300)
	release_date = models.DateField(null=True, blank=True)
	length = models.CharField(max_length=128, blank=True)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


	class Meta:
		verbose_name_plural = "Album's"

	def __str__(self):
		return '{}: {}'.format(self.artist, self.title)



class Song(models.Model):

	"""
	Song model maintains the information realted to a song
	@rtwhitfield84

	"""

	title = models.CharField(max_length=300)
	release_date = models.DateField(null=True, blank=True)
	length = models.CharField(max_length=128, blank=True)
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


	class Meta:
		verbose_name_plural = 'Songs'

	def __str__(self):
		return '{}, by {}, on the album {}'.format(self.title, self.artist, self.album)
























