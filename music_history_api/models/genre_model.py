from django.db import models

class Genre(models.Model):
	"""
	genre model maintains the information realted to a genre
	@rtwhitfield84

	"""

	NONE = ''
	ALTERNATIVE = 'Alternative'
	ROCK = 'Rock'
	FOLK = 'Folk'
	JAZZ = 'Jazz'
	CLASSICAL = 'Classical'
	POP = 'Pop'


	GENRE_CHOICES = (
		(NONE, ''),
		(ALTERNATIVE, 'Alternative'),
		(ROCK, 'Rock'),
		(FOLK, 'Folk'),
		(JAZZ, 'Jazz'),
		(CLASSICAL, 'Classical'),
		(POP, 'Pop'),

	)

	name = models.CharField(max_length=16, choices=GENRE_CHOICES, default=NONE)

	class Meta:
		verbose_name_plural = 'Genres'

	def __str__(self):
		return '{}'.format(self.name)