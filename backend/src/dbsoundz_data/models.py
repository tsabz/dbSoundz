from django.db import models

# Create your models here.


class Data(models.Model):
    artist_name = models.CharField(max_length=100)
    artist_genre = models.CharField(max_length=100)
    artist_notes = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title
