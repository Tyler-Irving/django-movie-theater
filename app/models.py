from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

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
    purchased_at = models.DateTimeField(default=timezone.now())
    showing = models.ForeignKey(Showing, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse("ticket_detail", kwargs={"id": self.id})

