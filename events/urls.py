from django.conf import settings
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static

from django.contrib import admin

from .views import EventCreateView, EventUpdateView, EventDeleteView, HomeView, DayView
from .views import ReservationView, ThankView

urlpatterns = [
    url(r"^$", HomeView.as_view(), name="home"),

    url(r"^(?P<year>\d{4})/(?P<month>\d{1,2})/$", HomeView.as_view(), name="monthly"),
    url(r"^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$", DayView.as_view(), name="daily"),

    #url(r"^admin/", include(admin.site.urls)),
    url(r'^admin/', admin.site.urls),
    url(r"^account/", include("account.urls")),

    url(r"^events/$", EventCreateView.as_view(), name="event_create"),
    url(r"^events/(?P<pk>\d+)/edit/$", EventUpdateView.as_view(), name="event_update"),
    url(r"^events/(?P<pk>\d+)/delete/$", EventDeleteView.as_view(), name="event_delete"),
    url(r"^reservation/", ReservationView.as_view(), name="contact"),
    url(r"^thanks/", ThankView.as_view(), name="thanks"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
