from django.contrib.auth.models import User
from django.db import models

class Artist(models.Model):
	"""
	Artist model maintains the information realted to an artist
	@rtwhitfield84

	"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	year_established = models.CharField(max_length=4, blank=True)
	label = models.CharField(max_length=128, blank=True)

	class Meta:
		verbose_name_plural = 'Artists'

	def __str__(self):
		return '{}'.format(self.name)