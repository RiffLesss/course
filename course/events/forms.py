from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',  'password1', 'password2']
