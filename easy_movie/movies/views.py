from django.shortcuts import render

from django.contrib.auth.models import User
from movies.models import Category, Actor, Producer, Realisator, Movie, MovieState
from django.contrib.auth.decorators import login_required


def home(request):
	movies = Movie.objects.get(id=1)
	#def get_mark(movie):
		#movies = MovieState.objects.select(movie = movie)
		#marks = [x.note for x in movies]
		#return sum(marks)/len(marks)
	#movies = Movie.objects.all()
	#movies = sorted([(get_mark(x), x) for x in movies])
	#movies = movies[-5:]
	return render(request, r"movies/index.html", {"movies" : movies})

@login_required
def notation(request):
	if request.GET:
		try:
			movie = Movie.objects.get(id=1)
			user = User.objects.get(id=1)
			rel = MovieState.objects.get(movie=movie, user=user)
		except:
			rel = []
		return render(request, r"movies/notation.html", {"rel":rel})
	elif request.POST:
		user = Movie.object.get(id=1)
		movie = request.POST['titre']
		note = request.POST['note']
		new_rel = MovieState(note=note, user=user, movie=movie)
		new_rel.save()
	return render(request, r"movies/notation.html")

def connection(request):    # Plusieurs fois la même fonction juste pour initialiser les views 
	movies = Movie.objects.get(id=1)
	return render(request, r"movies/connection.html", {"movies" : movies})

def inscription(request):
	movies = Movie.objects.get(id=1)
	return render(request, r"movies/inscription.html", {"movies" : movies})
@login_required
def reponseRecherche(request):
	movies = Movie.objects.get(id=1)
	return render(request, r"movies/reponseRecherche.html", {"movies" : movies})
@login_required
def espacePerso(request):
	movies = Movie.objects.get(id=1)
	return render(request, r"movies/espacePerso.html", {"movies" : movies})

def aPropos(request):
	return render(request, r"movies/aPropos.html")