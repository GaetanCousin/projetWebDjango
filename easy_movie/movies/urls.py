from django.conf.urls import patterns, url

urlpatterns = patterns("movies.views",
	url(r"^$","home"),
	)