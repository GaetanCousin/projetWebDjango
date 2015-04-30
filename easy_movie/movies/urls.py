from django.conf.urls import patterns, url

urlpatterns = patterns("movies.views", # movies/toto indice 0 et la View indice 1
	url(r"^$","home"),
	#url(r"^(?P<id>\d+)", "movie"), # SOUCIS EN PARLER A MATTHIEU
	url(r"notation", "notation"),
	url(r"connection", "connection"),
	url(r"inscription", "inscription"),
	url(r"reponse", "reponseRecherche"),
	url(r"espacePerso", "espacePerso"),
	url(r"aPropos", "aPropos")
	)