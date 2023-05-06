from django.forms import ModelForm
from .models import *

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'