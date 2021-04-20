#from datetime import date
from django import forms
from django.core.mail import send_mail
from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput
from events.models import Reservation


class ReservationForm(forms.Form):
    nom = forms.CharField()
    email = forms.EmailField()
    arrivee = forms.DateTimeField(
        widget=DateTimePickerInput(format='%d/%m/%Y'), label='Arrivée'
    )
    depart = forms.DateTimeField(
        widget=DateTimePickerInput(format='%d/%m/%Y'), label='Départ'
    )
    commentaires = forms.CharField(widget=forms.Textarea, required=False)
    def send_email(self):
        sujet = "Reservation"
        body = """                Bonjour,\n
        Une demande de réservation de l'appartement de St Etiennes a été \n
        effectuée depuis le site de l'amicale par {} ({}) pour la période \n
        du {} au {}\n
        \n
        ********commentaires********\n
        {}\n
        ****************************""".format(
            self.cleaned_data['nom'], self.cleaned_data['email'],
            self.cleaned_data['arrivee'].strftime("%d/%m/%Y"),
            self.cleaned_data['depart'].strftime("%d/%m/%Y"),
            self.cleaned_data['commentaires']
        )
        sender = "amicalespcontes@gmail.com"
        recipient = ["vince06fr@gmail.com", "cyrsp@hotmail.fr"]  #, "riva.georges@gmail.com"]
        send_mail(sujet, body, sender, recipient, fail_silently=False)

    def reservation(self):
        nom = self.cleaned_data['nom']
        email = self.cleaned_data['email']
        date_debut = self.cleaned_data['arrivee']
        date_fin = self.cleaned_data['depart']
        Reservation(
            nom=nom, email=email, date_debut=date_debut, date_fin=date_fin,
            confirmed=False
        ).save()
