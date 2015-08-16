from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User



class Artist(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    bio = models.TextField()
    profileImg = models.ImageField(upload_to="media/artist/profileImg", default="media/artist/profileImg/default.jpg")
    coverImg = models.ImageField(upload_to="media/artist/coverImg", default="media/artist/coverImg/default.jpg")
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.name


class Album(models.Model):
    name = models.CharField(max_length=30)
    artistID = models.ManyToManyField(Artist)
    description = models.TextField()
    price = models.IntegerField()
    licenseNo = models.CharField(max_length=50)
    publishDate = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s by %s' % (self.name, str(self.artistID))


class Track(models.Model):
    name = models.CharField(max_length=30)
    artistID = models.ManyToManyField(Artist)
    albumID = models.ForeignKey(Album)
    link = models.FileField(upload_to="")
    rateCount = models.IntegerField()
    rate = models.IntegerField(default=0, choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),))
    lyric = models.TextField(blank=True)
    poet = models.TextField(blank=True)
    price = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s by %s' % (self.name, str(self.artistID))


class User(AbstractBaseUser):
    userName = models.CharField(max_length=30, unique=Track, primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)
    balance = models.IntegerField(default=0)
    isGold = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    lastLogin = models.DateTimeField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'userName'
    REQUIRED_FIELDS = ["userName", "email"]

    def __unicode__(self):
        return u'%s' % self.userName

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.userName


class Playlist(models.Model):
    userID = models.ForeignKey(User)
    trackID = models.ForeignKey(Track)
    albumID = models.ForeignKey(Album)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'{%s} bought {%s} from {%s} album' % (str(self.trackID), str(self.trackID), self(self.albumID))

    class Meta:
        unique_together = (("userID", "trackID"),)


class Event:
    title=models.CharField(max_length=50)
    artistID=models.ForeignKey(Artist)
    description=models.TextField()
    location=models.TextField()
    pointLat=models.IntegerField()
    PointLon=models.IntegerField()
    data=models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=50)
    artistID = models.ForeignKey(Artist)
    content = models.TextField()
    likeCount = models.IntegerField(default=0)
    isPublic = models.BooleanField(default=True)
    isGeneral = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return r'post : %s' % self.title


class Comment(models.Model):
    postID = models.ForeignKey(Post)
    userID = models.ForeignKey(User)
    message = models.TextField()
    isConfirmed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return r'comment by %s' % str(self.userID)


class BankTransaction(models.Model):
    userID = models.ForeignKey(User)
    date = models.DateTimeField()
    amount = models.IntegerField()
    bank = models.CharField(max_length=20)
    receiptNo = models.CharField(max_length=30)
    createdAt = models.DateTimeField(auto_now_add=True)


class SiteTransaction(models.Model):
    userID = models.ForeignKey(User)
    date = models.DateTimeField()
    amount = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)


class Admin(AbstractBaseUser):
    userName = models.CharField(primary_key=True,unique=True,max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    balance = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'userName'
    REQUIRED_FIELDS = ["userName", "email"]


class AlbumOwner(models.Model):
    albumID = models.ForeignKey(Album)
    adminID = models.ForeignKey(Admin)
    percent = models.IntegerField()                                         #needed a restriction in data
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
