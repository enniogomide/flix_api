from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='movies'
    )
    released_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(
        Actor,
        related_name='moveis'
    )
    resume = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
