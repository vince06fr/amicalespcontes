#from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from bootstrap_datepicker_plus.widgets import DatePickerInput
from events.models import Reservation, ReservationEmailSettings


class ReservationForm(forms.Form):
    nom = forms.CharField()
    email = forms.EmailField()
    arrivee = forms.DateField(
        widget=DatePickerInput(format='%d/%m/%Y'), label='Arrivée'
    )
    depart = forms.DateField(
        widget=DatePickerInput(format='%d/%m/%Y'), label='Départ'
    )
    heure_arrivee = forms.ChoiceField(
        choices=[("13:00", "13h00")],
        initial="13:00",
        label="Heure d'arrivée",
    )
    heure_depart = forms.ChoiceField(
        choices=[("12:00", "midi")],
        initial="12:00",
        label="Heure de départ",
    )
    commentaires = forms.CharField(widget=forms.Textarea, required=False)
    def send_email(self):
        settings_obj = ReservationEmailSettings.objects.first()
        if not settings_obj:
            raise ValidationError("La configuration d'envoi d'email n'est pas définie. Merci de contacter l'administrateur.")
        sender = settings_obj.from_email
        recipients = [addr.strip() for addr in settings_obj.to_emails.split(",") if addr.strip()]
        reply_to = None

        sujet = "Reservation"
        body = """                Bonjour,\n
        Une demande de réservation de l'appartement de St Etiennes a été \n
        effectuée depuis le site de l'amicale par {} ({}) pour la période \n
        du {} au {}\n
        Heure d'arrivée : {}\n
        Heure de départ : {}\n
        \n
        ********commentaires********\n
        {}\n
        ****************************""".format(
            self.cleaned_data['nom'], self.cleaned_data['email'],
            self.cleaned_data['arrivee'].strftime("%d/%m/%Y"),
            self.cleaned_data['depart'].strftime("%d/%m/%Y"),
            "13h00",
            "midi",
            self.cleaned_data['commentaires']
        )
        send_mail(sujet, body, sender, recipients, fail_silently=False)

    def reservation(self):
        nom = self.cleaned_data['nom']
        email = self.cleaned_data['email']
        date_debut = self.cleaned_data['arrivee']
        date_fin = self.cleaned_data['depart']
        heure_arrivee = self.cleaned_data['heure_arrivee']
        heure_depart = self.cleaned_data['heure_depart']
        Reservation(
            nom=nom, email=email, date_debut=date_debut, date_fin=date_fin,
            heure_arrivee=heure_arrivee, heure_depart=heure_depart,
            confirmed=False
        ).save()

    def clean(self):
        cleaned = super().clean()
        arrivee = cleaned.get("arrivee")
        depart = cleaned.get("depart")
        if arrivee and depart and depart <= arrivee:
            raise ValidationError("La date de départ doit être au moins le lendemain de la date d'arrivée.")

        settings_obj = ReservationEmailSettings.objects.first()
        if not settings_obj:
            raise ValidationError("L'envoi d'email n'est pas configuré. Merci de contacter l'administrateur.")
        recipients = [addr.strip() for addr in settings_obj.to_emails.split(",") if addr.strip()] if settings_obj else []
        if not settings_obj.from_email or not recipients:
            raise ValidationError("L'envoi d'email n'est pas configuré correctement. Merci de contacter l'administrateur.")
        return cleaned
