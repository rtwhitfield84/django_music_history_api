from django.contrib.auth.models import User
from django.db import models
from music_history_api.models import album_model, genre_model,artist_model

class Song(models.Model):

	"""
	Song model maintains the information realted to a song
	@rtwhitfield84

	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=300)
	release_date = models.DateField(null=True, blank=True)
	length = models.CharField(max_length=128, blank=True)
	album = models.ForeignKey(album_model.Album, on_delete=models.CASCADE)
	genre = models.ForeignKey(genre_model.Genre, on_delete=models.CASCADE,null=True, blank=True)
	artist = models.ForeignKey(artist_model.Artist, on_delete=models.CASCADE)


	class Meta:
		verbose_name_plural = 'Songs'

	def __str__(self):
		return '{}, by {}, on the album {}'.format(self.title, self.artist, self.album)
