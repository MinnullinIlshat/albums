#apis/views.py
from rest_framework import generics 

from albums.models import Album
from .serializers import AlbumSerializer 


class AlbumAPIView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer