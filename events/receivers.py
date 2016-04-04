from django.dispatch import receiver

from account.signals import password_changed
from account.signals import user_sign_up_attempt, user_signed_up
from account.signals import user_login_attempt, user_logged_in

from pinax.eventlog.models import log


from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.contrib.auth.models import User
from events.models import Event, Reservation
from datetime import datetime, timedelta


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

######################################################
@receiver(pre_save, sender=Reservation)
def reservation_pre_save(sender, **kwargs):
    print('pre_save: {}'.format(kwargs['instance'].__dict__))

@receiver(post_save, sender=Reservation)
def reservation_post_save(sender, **kwargs):
    # si user n'est pas connecté
    user = User.objects.get(username='admin')
    # sinon si user est connecté
    # user = request.user
    if  kwargs['instance'].confirmed == False:
        nom = '?' + kwargs['instance'].nom + '?'
    else:
        nom = kwargs['instance'].nom

    email = kwargs['instance'].email
    date_debut = kwargs['instance'].date_debut
    date_fin = kwargs['instance'].date_fin

    jour = datetime.date(date_debut)

    while jour < date_fin or jour == date_fin:
        Event(title=nom, date=jour, created_by=user).save()
        jour += timedelta(days=1)
    print('Saved: {}'.format(kwargs['instance'].__dict__))

@receiver(pre_delete, sender=Reservation)
def model_pre_delete(sender, **kwargs):
    print('pre_delete: {}'.format(kwargs['instance'].__dict__))

@receiver(post_delete, sender=Reservation)
def model_post_delete(sender, **kwargs):
    print('Deleted: {}'.format(kwargs['instance'].__dict__))
