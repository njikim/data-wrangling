from django.shortcuts import render
from django.http.response import HttpResponse
from baseapp.models import Movie
from baseapp.makedf import sortbysales
# Create your views here.
def home(request):
    return render(request, 'home.html')

def genre(request):
    return render(request, 'genre.html')

def genre_result(request):
    selected = request.GET.get("selected")
    movie_list = Movie.objects.filter(genre__contains=selected)
    movie_sorted = sortbysales(movie_list)
    #print(type(movie_sorted))
    print(movie_sorted)
    
    dbcontent = {
        "selected":selected,
        "movie_list": movie_list,
        "movie_sorted" : movie_sorted
    }
    return render(request, 'genre_result.html', dbcontent)