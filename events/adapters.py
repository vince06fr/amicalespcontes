from collections import defaultdict

import pytz
from pinax.calendars.adapters import EventAdapter as BaseEventAdapter


class EventAdapter(BaseEventAdapter):
    """
    Adapter local pour supporter les DateField (sans timezone).
    Évite l'appel à .astimezone() sur des objets datetime.date.
    """

    def events_by_day(self, year, month, tz, **kwargs):
        days = defaultdict(list)
        query_args = {
            f"{self.date_field_name}__year": year,
            f"{self.date_field_name}__month": month,
        }
        timezone = pytz.timezone(tz) if tz else pytz.utc

        for event in self.events.filter(**query_args).order_by(self.date_field_name):
            value = getattr(event, self.date_field_name)
            if hasattr(value, "astimezone"):
                day = value.astimezone(timezone).day
            else:
                day = value.day
            days[day].append(event)
        return days
