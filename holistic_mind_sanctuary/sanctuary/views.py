from django.shortcuts import render

from django.shortcuts import render
from .models import Zone, Service, Event, Post


def home(request):
    return render(request, 'home.html')





