from django.db import models



class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.SmallIntegerField()

    def __str__(self):
        return f'{self.name}[{self.year}]'
    

class Track(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    