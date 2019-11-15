from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
from django.http import HttpRequest
from app.models import Movie, Ticket, Showing
from app.forms import NewTicketForm


# Create your views here.


class MovieListView(generic.ListView):
    model = Movie
    context_object_name = "movies"
    template_name = "home.html"


class NewTicketView(generic.CreateView):
    model = Ticket
    fields = ["name", "showing"]
    template_name = "new_ticket.html"
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.request.resolver_match.kwargs['id']
        movie = Movie.objects.get(id=id)
        context['movie'] = movie
        return context


class TicketDetailView(generic.DetailView):
    model = Ticket
    context_object_name = "ticket"
    template_name = "ticket_detail.html"
    pk_url_kwarg = "id"
