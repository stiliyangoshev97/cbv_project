from django.db import models
from django.urls import reverse

# Create your models here.

class Song(models.Model):
	name = models.CharField(max_length = 256)
	artist = models.CharField(max_length = 256)
	year = models.PositiveIntegerField()

	def __str__(self):
		return self.name + ' - ' + self.artist

		# Absolute URL Method to affect the details of Song class

	def get_absolute_url(self):
		return reverse('cbv_app:detail', kwargs={'pk':self.pk})

class Detail(models.Model):
	genre = models.CharField(max_length = 256)
	song = models.ForeignKey(Song, related_name = 'details', on_delete = models.CASCADE)

	def __str__(self):
		return self.genre







