from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Songs(models.Model):
    file_type = models.CharField(max_length=20)
    song_title = models.CharField(max_length=250)
    date = models.CharField(max_length=250,default="", editable=True)
    time = models.CharField(max_length=250,default="", editable=True)
    def __str__(self):
        return self.song_title
