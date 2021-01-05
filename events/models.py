from django.db import models
from six import python_2_unicode_compatible

from django.contrib.auth.models import User


@python_2_unicode_compatible
class Reservation(models.Model):

    nom = models.CharField(max_length=100)
    email = models.EmailField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.nom


@python_2_unicode_compatible
class Event(models.Model):

    title = models.CharField(max_length=100)
    date = models.DateField()
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    reservation = models.ForeignKey(Reservation, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
