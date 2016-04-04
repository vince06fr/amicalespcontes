from django.contrib import admin
from events.models import Event, Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'date_debut', 'date_fin', 'confirmed')
    date_hierarchy = 'date_debut'
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Event)
