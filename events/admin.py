from django.contrib import admin
from events.models import Event, Reservation


def set_reservation_validate(modeladmin, request, queryset):
    queryset.update(confirmed=True)
    for event in queryset:
        event.save()
set_reservation_validate.short_description = "Valider les reservations sélectionnées"

def set_reservation_unvalidate(modeladmin, request, queryset):
    queryset.update(confirmed=False)
    for event in queryset:
        event.save()
set_reservation_unvalidate.short_description = "Annuler la validation des reservations sélectionnées"


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'date_debut', 'date_fin', 'confirmed')
    date_hierarchy = 'date_debut'
    actions = [set_reservation_validate, set_reservation_unvalidate]
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Event)
