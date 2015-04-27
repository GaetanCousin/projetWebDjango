from django.shortcuts import render

from django.contrib.auth.models import User
from movies.models import Category, Actor, Producer, Realisator, Movie, MovieState

def home(request):
	#if request.GET:
		try:
			movie = Movie.objects.get(id=1)
			user = User.objects.get(id=1)
			rel = MovieState.objects.get(movie=movie, user=user)
		except:
			rel = []
		print(rel)
		return render(request, r"movies/notation.html", {"rel":rel})
	#elif request.POST:
	#	movie = 
	#	note = 
	#	new_rel = MovieState(note=note, user=user, movie=movie)
	#	new_rel.save()

def index(request):
	def get_mark(movie):
		movies = MovieState.objects.select(movie = movie)
		marks = [x.note for x in movies]
		return sum(marks)/len(marks)
	movies = Movie.objects.all()
	movies = sorted([(get_mark(x), x) for x in movies])
	movies = movies[-5:]
	return render(request, r"movies/index.html", {"movies" : movies})