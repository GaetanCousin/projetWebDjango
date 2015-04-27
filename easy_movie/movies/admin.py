from django.contrib import admin

from movies.models import Category, Actor, Producer, Realisator, Movie, MovieState

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class ActorAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'surname')

class ProducerAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'surname')

class RealisatorAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'surname')

class MovieAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date_out')

class MovieStateAdmin(admin.ModelAdmin):
	list_display = ('id',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Realisator, RealisatorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieState, MovieStateAdmin)