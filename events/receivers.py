from django.dispatch import receiver

from account.signals import password_changed
from account.signals import user_sign_up_attempt, user_signed_up
from account.signals import user_login_attempt, user_logged_in

from pinax.eventlog.models import log


from django.db.models.signals import pre_save, post_save
from events.models import Event, Reservation
from datetime import timedelta


@receiver(user_logged_in)
def handle_user_logged_in(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="USER_LOGGED_IN",
        extra={}
    )


@receiver(password_changed)
def handle_password_changed(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="PASSWORD_CHANGED",
        extra={}
    )


@receiver(user_login_attempt)
def handle_user_login_attempt(sender, **kwargs):
    log(
        user=None,
        action="LOGIN_ATTEMPTED",
        extra={
            "username": kwargs.get("username"),
            "result": kwargs.get("result")
        }
    )


@receiver(user_sign_up_attempt)
def handle_user_sign_up_attempt(sender, **kwargs):
    log(
        user=None,
        action="SIGNUP_ATTEMPTED",
        extra={
            "username": kwargs.get("username"),
            "email": kwargs.get("email"),
            "result": kwargs.get("result")
        }
    )


@receiver(user_signed_up)
def handle_user_signed_up(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="USER_SIGNED_UP",
        extra={}
    )


@receiver(pre_save, sender=Reservation)
def reservation_pre_save(sender, **kwargs):
    """clean Event before saving reservation."""
    events = Event.objects.all()
    for event in events:
        if event.reservation == kwargs['instance']:
            event.delete()


@receiver(post_save, sender=Reservation)
def reservation_post_save(sender, **kwargs):
    """bash add Event following Reservation period."""

    if kwargs['instance'].confirmed is False:
        nom = '??' + kwargs['instance'].nom + '??'
    else:
        nom = kwargs['instance'].nom

    date_debut = kwargs['instance'].date_debut
    date_fin = kwargs['instance'].date_fin
    jour = date_debut

    while jour < date_fin or jour == date_fin:
        Event(title=nom, date=jour, reservation=kwargs['instance'], confirmed = kwargs['instance'].confirmed).save()
        jour += timedelta(days=1)
