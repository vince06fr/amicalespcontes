from django.conf import settings
from django.urls import path, re_path, include
#from django.conf.urls import include, url
from django.conf.urls.static import static

from django.contrib import admin

from .views import EventCreateView, EventUpdateView, EventDeleteView, HomeView, DayView
from .views import ReservationView, ThankView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    re_path(r"^(?P<year>\d{4})/(?P<month>\d{1,2})/$", HomeView.as_view(), name="monthly"),
    re_path(r"^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$", DayView.as_view(), name="daily"),

    path('admin/', admin.site.urls),
    path("account/", include("account.urls")),

    path("events/", EventCreateView.as_view(), name="event_create"),
    re_path(r"^events/(?P<pk>\d+)/edit/$", EventUpdateView.as_view(), name="event_update"),
    re_path(r"^events/(?P<pk>\d+)/delete/$", EventDeleteView.as_view(), name="event_delete"),
    path("reservation/", ReservationView.as_view(), name="contact"),
    path("thanks/", ThankView.as_view(), name="thanks"),
]


if settings.DEBUG:  # pragma: no cover
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
