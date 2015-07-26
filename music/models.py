from django.db import models

#test
class Artist(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    bio = models.TextField()
    profileImg = models.ImageField(upload_to="media/artist/profileImg", default="media/artist/profileImg/default.jpg")
    coverImg = models.ImageField(upload_to="media/artist/coverImg", default="media/artist/coverImg/default.jpg")


class Album(models.Model):
    name = models.CharField(max_length=30)
    artistID = models.ForeignKey(Artist)
    description = models.TextField()
    price = models.IntegerField()
    licenseNo = models.CharField(max_length=50)


class Track(models.Model):
    name = models.CharField(max_length=30)
    artistID = models.ManyToManyField(Artist)
    albumID = models.ForeignKey(Album)
    link = models.FileField(upload_to="")
    rate = models.IntegerField(default=0, choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),))
    lyric = models.TextField(blank=True)
    poet = models.TextField(blank=True)
    price = models.IntegerField()


class User(models.Model):
    userName = models.CharField(max_length=30, unique=True, primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)
    balance = models.IntegerField(default=0)
    isGold = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    lastLogin = models.DateTimeField(blank=True)


class Playlist(models.Model):
    userID = models.ForeignKey(User)
    trackID = models.ForeignKey(Track)
    albumID = models.ForeignKey(Album)

    class Meta:
        unique_together = (("userID", "trackID"),)
