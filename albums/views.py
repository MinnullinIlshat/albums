from django.shortcuts import render
from .models import Album
from django.http import HttpResponse
# Create your views here.

l = [{
"album": "album1[2022]",
"name":"album1",
"artist@name":"artist_name1",
"tracks":["track1","track2","track3"]
}]

def home_page(request):
    return HttpResponse(f'<h1>Hello world</h1><p>{l}</p>')