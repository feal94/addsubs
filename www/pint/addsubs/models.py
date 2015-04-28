from django.db import models

class Job(models.Model):
	user = models.CharField(max_length=50)
	video = models.CharField(max_length=100)
	language = models.CharField(max_length=100)
	delay = models.IntegerField()
	play = models.BooleanField()

	def __unicode__(self):
		return self.user + ": " + self.video


class Movie(models.Model):
	title = models.CharField(max_length=50)
	director = models.CharField(max_length=50)
	year = models.IntegerField()
	hash = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title + ": " + self.year
