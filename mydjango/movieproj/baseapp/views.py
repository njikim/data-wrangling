from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def genre(request):
    return render(request, 'genre.html')