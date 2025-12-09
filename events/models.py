from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):

    nom = models.CharField(max_length=100)
    email = models.EmailField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    heure_arrivee = models.TimeField(default="13:00")
    heure_depart = models.TimeField(default="12:00")
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.nom


class ReservationEmailSettings(models.Model):
    """
    Paramètres de notification pour les réservations (configurables en admin).
    Singleton : une seule instance attendue.
    """

    from_email = models.EmailField()
    to_emails = models.TextField(help_text="Liste d'adresses séparées par des virgules.")
    singleton = models.BooleanField(default=True, unique=True, editable=False)

    def __str__(self):
        return "Paramètres email des réservations"


class Event(models.Model):

    title = models.CharField(max_length=100)
    date = models.DateField()
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    reservation = models.ForeignKey(Reservation, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
