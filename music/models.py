from django.db import models


class Artist(models.Model):
    name = models.CharField()


class Track(models.Model):
    name = models.CharField()
