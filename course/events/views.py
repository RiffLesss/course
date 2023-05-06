from django.shortcuts import render, redirect

from .models import *
from .forms import *

def student(request):
    events = Event.objects.all()
    content = {'events': events}
    return render(request, 'events/student.html', content)

def activities(request, id):
    event = Event.objects.get(id=id)
    activities = Activity.objects.filter(event=event)
    content = {'event': event, 'activities': activities}
    return render(request, 'events/activities.html', content)

def myevents(request):
    events = Event.objects.all()
    return render(request, 'events/myevents.html', {'events': events})

def create_event(request):

    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'events/create_event.html', context)

def create_activity(request):

    form = ActivityForm()
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'events/create_activity.html', context)

def update_event(request, id):

    event = Event.objects.get(id=id)
    form = EventForm(instance=event)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'events/create_event.html', context)

def update_activity(request, id):

    activity = Activity.objects.get(id=id)
    form = ActivityForm(instance=activity)
    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'events/create_activity.html', context)

def delete_event(request, id):
    event = Event.objects.get(id=id)
    if request.method == "POST":
        event.delete()
        return redirect('/')
    context = {'event': event}
    return render(request, 'events/delete_event.html', context)

def delete_activity(request, id):
    activity = Activity .objects.get(id=id)
    redir = '/event/' + str(activity.event.id)
    if request.method == "POST":
        activity.delete()
        return redirect(redir)
    context = {'activity': activity}
    return render(request, 'events/delete_activity.html', context)