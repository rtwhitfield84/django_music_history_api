from django.contrib.auth.models import User
from django.db import models
from music_history_api.models import artist_model, genre_model


class Album(models.Model):
	"""
	Album model maintains the information realted to an album
	@rtwhitfield84

	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=300)
	release_date = models.DateField(null=True, blank=True)
	length = models.CharField(max_length=128,null=True, blank=True)
	artist = models.ForeignKey(artist_model.Artist, on_delete=models.CASCADE)
	genre = models.ForeignKey(genre_model.Genre, on_delete=models.CASCADE, null=True, blank=True)


	class Meta:
		verbose_name_plural = "Albums"

	def __str__(self):
		return '{}: {}'.format(self.artist, self.title)
