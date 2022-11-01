from rest_framework import serializers 

from albums.models import Album, Artist, Track

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist 
        fields = ("name",)

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track 
        fields = ("name", "album")

class AlbumSerializer(serializers.ModelSerializer):
    album = serializers.SerializerMethodField()
    artist = ArtistSerializer()
    tracks = serializers.StringRelatedField(many=True)

    def get_album(self, album):
        return str(album)

    class Meta:
        model = Album 
        fields = ("album", "name", "artist", "tracks")