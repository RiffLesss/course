from django.urls import path
from . import views

urlpatterns = [
    path('', views.student),
    path('events/', views.events),
    path('activities/', views.activities),
    path('myevents/', views.myevents),
]
