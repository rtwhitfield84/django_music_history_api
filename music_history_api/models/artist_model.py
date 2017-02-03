from django.db import models


class Artist(models.Model):
	"""
	Artist model maintains the information realted to an artist
	@rtwhitfield84

	"""
	name = models.CharField(max_length=128)
	year_established = models.CharField(max_length=4, null=True, blank=True)
	label = models.CharField(max_length=128, null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Artists'

	def __str__(self):
		return '{}'.format(self.name)