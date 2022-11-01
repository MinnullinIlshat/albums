#albums/views.py
from django.shortcuts import render 
import requests 


def index(request, sort_by=None):
    responses = requests.get('http://127.0.0.1:8000/api/').json()
    if sort_by == 'album_name':
        key = lambda x: x['name']
        responses = sorted(responses, key=key)
    elif sort_by == 'artist_name':
        key = lambda x: x['artist']['name']
        responses = sorted(responses, key=key)
    return render(request, 'albums/index.html', {'responses': responses})