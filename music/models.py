from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Artist(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    title = models.CharField(max_length=50)
    bio = models.TextField()
    weblog = models.CharField(max_length=100, default='#')
    website = models.CharField(max_length=100, default='#')
    rss = models.CharField(max_length=100, default='#')
    youtube = models.CharField(max_length=100, default='#')
    facebook = models.CharField(max_length=100, default='#')
    twitter = models.CharField(max_length=100, default='#')
    backImg = models.ImageField(upload_to="music/artist/backimg", default="music/artist/backimg/default.jpg")
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class ArtistPoster(models.Model):
    artistID = models.ForeignKey(Artist)
    img = models.ImageField(upload_to="music/artistposter/img", default="music/artistposter/img/default.jpg")


class Album(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    artistID = models.ManyToManyField(Artist)
    mainTrack = models.OneToOneField('Track', blank=True, null=True)
    publisherName = models.CharField(max_length=30)
    website = models.CharField(max_length=100, blank=True, null=True)
    style = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    downloads = models.IntegerField(default=0)
    licenseNo = models.CharField(max_length=50)
    publishDate = models.DateTimeField()
    visits = models.IntegerField(default=0)
    sliderImg = models.ImageField(upload_to="music/album/sliderImg", default="music/album/sliderImg/default.jpg")
    thumbImg = models.ImageField(upload_to="music/album/thumbImg", default="music/album/thumbImg/default.jpg")
    backImg = models.ImageField(upload_to="music/album/backImg", default="music/album/backImg/default.jpg")
    iconImg = models.ImageField(upload_to="music/album/iconImg", default="music/album/iconImg/default.jpg")
    publisherImg = models.ImageField(upload_to="music/album/publisherImg",
                                     default="music/album/publisherImg/default.jpg")
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return u'%s by %s' % (self.name, str(self.artistID))

    def __str__(self):
        return self.name


class AlbumCover(models.Model):
    albumID = models.ForeignKey(Album)
    img = models.ImageField(upload_to="music/albumcover/img", default="music/albumcover/img/default.jpg")


class Advertise(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    link = models.CharField(max_length=100, default="#")
    position = models.CharField(max_length=20, default="home")
    img = models.ImageField(upload_to="music/advertise/img", default="music/advertise/img/default.jpg")
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Track(models.Model):
    name = models.CharField(max_length=30)
    artistID = models.ManyToManyField(Artist)
    albumID = models.ForeignKey(Album)
    link = models.FileField(upload_to="music/track/link")
    rateCount = models.IntegerField()
    rate = models.IntegerField(default=0, choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),))
    lyric = models.TextField(blank=True)
    poet = models.TextField(blank=True)
    price = models.IntegerField()
    playerImg = models.ImageField(upload_to="music/track/playerimg", default="music/track/playerimg/default.jpg")
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s by %s' % (self.name, str(self.artistID))


class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=Track, primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)
    balance = models.IntegerField(default=0)
    isGold = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    profileImg = models.ImageField(upload_to="user/profileimg", default="user/profileimg/default.jpg")
    lastLogin = models.DateTimeField(blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["username", "email"]

    def __unicode__(self):
        return u'%s' % self.username

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User,self).save(*args,**kwargs)


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
    title = models.CharField(max_length=50)
    artistID = models.ForeignKey(Artist)
    description = models.TextField()
    location = models.TextField()
    pointLat = models.IntegerField()
    PointLon = models.IntegerField()
    data = models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

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
    userName = models.CharField(primary_key=True, unique=True, max_length=50)
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
    percent = models.IntegerField()  # needed a restriction in data
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
