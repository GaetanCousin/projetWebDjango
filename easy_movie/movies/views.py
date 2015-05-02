from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from movies.models import Category, Actor, Producer, Realisator, Movie, MovieState
from django.contrib.auth.decorators import login_required
from movies.forms import ContactForm

def home(request):
	def get_mark(movie):
		movies = MovieState.objects.filter(movie=movie) 
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
		movie = request.POST.get('titre')
		note = request.POST.get('note')
		new_rel = MovieState(note=note, user=user, movie=movie)
		new_rel.save()
	return render(request, r"movies/notation.html")

def connection(request):   # Exemple pour le moment
    #username = request.POST['username']
   	#password = request.POST['password']
   # user = authenticate(username=username, password=password)
    #if user is not None:
     #   if user.is_active:
          #  login(request, user)
            # Redirect to a success page.
       # else:
            # Return a 'disabled account' error message
           # ...
   # else:
        # Return an 'invalid login' error message.
	return render(request, r"movies/connection.html")

def inscription(request):
    # Ici nous pouvons traiter les données du formulaire
    #nom = request.POST.get('adresse')
    #mdp = request.POST.get('mdp')
    user = User.objects.create_user('surname', 'email', 'password')
    user.save()
    # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
    return render(request, 'movies/inscription.html')



@login_required
def reponseRecherche(request):
	return render(request, r"movies/reponseRecherche.html")

@login_required
def espacePerso(request):
	return render(request, r"movies/espacePerso.html")

def aPropos(request):
	return render(request, r"movies/aPropos.html")