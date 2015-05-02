from django.shortcuts import render

from django.contrib.auth.models import User
from movies.models import Category, Actor, Producer, Realisator, Movie, MovieState
from django.contrib.auth.decorators import login_required


def home(request):
	#movies = Movie.objects.get(id=1)
	def get_mark(movie):
		movies = MovieState.objects.select(movie= movie) # erreur a ce niveau la je ne comprend pas pourquoi, ca fonctionne avec movies = MovieState.objects.all() mais ce n'est pas ce qu'on veut .. :S
		marks = [x.note for x in movies]
		return sum(marks)/len(marks) # len = nbr d'element
	movies = Movie.objects.all()
	moviesTrie = sorted([(get_mark(x), x.id) for x in movies])
	topMovies = moviesTrie[-5:]
	return render(request, r"movies/index.html", {"topMovies" : topMovies})

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
	if request.GET:
		return render(request, r"movies/inscription.html")
	elif request.POST:
		adresse = request.POST['adresse']
		mdp = request.POST['mdp']
		new_user = User(username=adresse, mdp=mdp)
		new_user.save()
	return render(request, r"movies/inscription.html")



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