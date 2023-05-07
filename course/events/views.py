from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'events/login.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

        context = {'form': form}
        return render(request, 'events/register.html', context)


def logout_user(request):
    print('logout')
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def student(request):
    events = Event.objects.all()
    content = {'events': events}
    return render(request, 'events/student.html', content)


@login_required(login_url='login')
def activities(request, id):
    event = Event.objects.get(id=id)
    activities = Activity.objects.filter(event=event)
    content = {'event': event, 'activities': activities}
    return render(request, 'events/activities.html', content)


@login_required(login_url='login')
def myevents(request):
    events = Event.objects.all()
    return render(request, 'events/myevents.html', {'events': events})


@login_required(login_url='login')
def create_event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'events/create_event.html', context)


@login_required(login_url='login')
def create_activity(request):
    form = ActivityForm()
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'events/create_activity.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_event(request, id):
    event = Event.objects.get(id=id)
    if request.method == "POST":
        event.delete()
        return redirect('/')
    context = {'event': event}
    return render(request, 'events/delete_event.html', context)


@login_required(login_url='login')
def delete_activity(request, id):
    activity = Activity.objects.get(id=id)
    redir = '/event/' + str(activity.event.id)
    if request.method == "POST":
        activity.delete()
        return redirect(redir)
    context = {'activity': activity}
    return render(request, 'events/delete_activity.html', context)
