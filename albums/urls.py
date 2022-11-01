# albums/urls.py 
from django.urls import path

from .views import index


urlpatterns = [ 
    path('', index, name='home'),
    path('sort_by/<str:sort_by>/', index, name='sort_by_album_name'),
    path('sort_by/<str:sort_by>/', index, name='sort_by_artist_name')
]