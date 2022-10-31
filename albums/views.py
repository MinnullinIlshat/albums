#albums/views.py
from django.views.generic import ListView 

from .models import Album


class AlbumListView(ListView):
    model = Album 
    template_name = 'album_list.html'