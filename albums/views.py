#albums/views.py
from django.shortcuts import render 
import requests 


def index(request):
    responses = requests.get('http://127.0.0.1:8000/api/').json()
    return render(request, 'albums/index.html', {'responses': responses})