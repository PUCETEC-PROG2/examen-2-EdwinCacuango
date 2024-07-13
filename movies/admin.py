from django.contrib import admin
from .models import Movie

# Register your models here.

@admin.register(Movie)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'gender', 'director_name', 'release_year', 'sinopsis')