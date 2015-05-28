from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
	title = models.CharField(max_length=50)
	director = models.CharField(max_length=50)
	year = models.IntegerField()
	hash = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title + ": " + self.year


class Job(models.Model):
	user = models.ForeignKey(User, unique=True)
	video = models.ForeignKey(Movie)
	language = models.CharField(max_length=100)
	delay = models.IntegerField()
	play = models.BooleanField()
	finished = models.BooleanField()

	def __unicode__(self):
		return self.user + ": " + self.video
