from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Actor(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	def __str__(self):
		return self.name +' '+ self.surname

class Producer(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	def __str__(self):
		return self.name +' '+ self.surname

class Realisator(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	def __str__(self):
		return self.name +' '+ self.surname

class Movie(models.Model):
	title = models.CharField(max_length=100) 
	duration = models.DurationField()
	date_out = models.DateField()
	category = models.ManyToManyField(Category)
	producer = models.ManyToManyField(Producer)
	realisator = models.ManyToManyField(Realisator)
	actors = models.ManyToManyField(Actor)
	state = models.ManyToManyField(User, through='MovieState')
	def __str__(self):
		return self.title

class MovieState(models.Model):
	note = models.BigIntegerField()
	user = models.ForeignKey(User)
	movie = models.ForeignKey(Movie)