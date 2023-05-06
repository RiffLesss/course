from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def student(request):
    events = Event.objects.all()
    return render(request, 'events/student.html', {'events': events})

def events(request):
    return render(request, 'events/events.html')

def activities(request):
    activities = Activity.objects.first()
    spots_left = activities.spots - activities.spots_taken
    return render(request, 'events/activities.html', {'activities': activities, 'spots_left': spots_left})

def myevents(request):
    events = Event.objects.all()
    return render(request, 'events/student.html', {'events': events})