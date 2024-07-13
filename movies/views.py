from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie
from django.template import loader
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render({'movies':movies}, request))


def details(request, movie):
    template = loader.get_template('details.html')
    movie = Movie.objects.get(title = movie)
    
    return HttpResponse(template.render({'movie':movie}, request))