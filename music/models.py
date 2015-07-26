from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    bio = models.TextField()
    profileImg = models.ImageField(upload_to="media/artist/profileImg")

class Track(models.Model):
    name = models.CharField()
