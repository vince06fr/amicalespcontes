from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView

from account.mixins import LoginRequiredMixin
from .adapters import EventAdapter
from pinax.calendars.mixins import DailyMixin, MonthlyMixin

from .models import Event

from .forms import ReservationForm
from django.views.generic.edit import FormView


class GoHomeMixin(object):

    def get_success_url(self):
        return reverse("home")


class OwnerMixin(object):

    def get_queryset(self):
        return self.model._default_manager.filter(created_by=self.request.user)


class HomeView(MonthlyMixin, TemplateView):

    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            "the_date": self.date,
            "events": EventAdapter(Event.objects.all())
        })
        return context


class DayView(DailyMixin, TemplateView):

    template_name = "daily.html"

    def get_context_data(self, **kwargs):
        context = super(DayView, self).get_context_data(**kwargs)
        context.update({
            "the_date": self.date,
            "events": Event.objects.filter(date=self.date)
        })
        return context


class EventCreateView(LoginRequiredMixin, OwnerMixin, GoHomeMixin, CreateView):
    model = Event
    fields = ["title", "date"]

    def form_valid(self, form):
        event = form.save(commit=False)
        event.created_by = self.request.user
        event.save()
        return redirect(self.get_success_url())


class EventUpdateView(LoginRequiredMixin, OwnerMixin, GoHomeMixin, UpdateView):
    model = Event
    fields = ["title", "date"]


class EventDeleteView(LoginRequiredMixin, OwnerMixin, GoHomeMixin, DeleteView):
    model = Event


class ReservationView(FormView):
    template_name = 'reservation.html'
    form_class = ReservationForm
    success_url = '/thanks/'
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        form.reservation()
        return super(ReservationView, self).form_valid(form)


class ThankView(TemplateView):
    template_name = 'thanks.html'
