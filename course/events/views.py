from django.shortcuts import render
from django.http import HttpResponse

def student(request):
    return render(request, 'events/student.html')

def events(request):
    return render(request, 'events/events.html')

#def activity(request):
#   return HttpResponse('Event page')
