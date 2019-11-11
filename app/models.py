from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    rating = models.TextField()
    genre = models.TextField()
    runtime = models.TextField()

class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    showtime = models.TextField()

class Ticket(models.Model):
    name = models.TextField()
    purchased_at = models.DateTimeField()
    showing = models.ForeignKey(Showing, on_delete=models.PROTECT)