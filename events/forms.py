from django import forms
from django.core.mail import send_mail
from datetime import date


class ReservationForm(forms.Form):
    nom = forms.CharField()
    email = forms.EmailField()
    arrivee = forms.DateField(input_formats=['%d-%m-%Y'], label="Arrivée", initial=date.today().strftime("%d-%m-%Y"))
    depart = forms.DateField(input_formats=['%d-%m-%Y'], initial=date.today().strftime("%d-%m-%Y"))
    commentaires = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        sujet = "Reservation"
        body = """Bonjour,\n
        Une demande de réservation de l'appartement de St Etiennes a été effectuée depuis le site de l'amicale par {} ({}) pour la période du {} au {}\n
        \n
        ********commentaires********\n
        {}\n
        ****************************""".format(self.cleaned_data['nom'], self.cleaned_data['email'], self.cleaned_data['arrivee'], self.cleaned_data['depart'], self.cleaned_data['commentaires'])
        sender = "amicalespcontes@gmail.com"
        recipient = ["vince06fr@gmail.com", "riva.georges@gmail.com"]
        send_mail(sujet, body, sender, recipient, fail_silently=False)