from django.db import models
from django.urls import reverse


class Place(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse(
        'place-detail', kwargs={'place_id': str(self.id)}
    )

    def __str__(self):
        return self.name
