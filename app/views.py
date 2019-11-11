from django.shortcuts import render, redirect
from django.utils import timezone
from app.models import Movie, Ticket, Showing
from app.forms import NewTicketForm


# Create your views here.


def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})


def new_ticket(request, id):
    if request.method == "GET":
        movie = Movie.objects.get(id=id)
        form = NewTicketForm()
        return render(request, "new_ticket.html", {"movie": movie, "form": form})
    elif request.method == "POST":
        form = NewTicketForm(request.POST)
        if form.is_valid():
            movie = Movie.objects.get(id=id)
            name = form.cleaned_data['name']
            showing_id = form.cleaned_data['showing_id']
            new_ticket = Ticket.objects.create(
                name=name, showing_id=movie.id, purchased_at=timezone.now()
            )
            new_ticket.save()
            return redirect("ticket_detail", movie.id)
        else:
            movie = Movie.objects.get(id=id)
            form = NewTicketForm()
            return render(request, "new_ticket.html", {"movie": movie, "form": form})


def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, "ticket_detail.html", {"ticket": ticket})
