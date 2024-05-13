from django.shortcuts import render

from django.shortcuts import render
from .models import Zone, Service, Event, Post


def home(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about_us.html')


def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})



