from django.urls import path
from . import views

urlpatterns = [
    path('', views.student, name="events"),
    path('event/<int:id>', views.activities, name="event"),
    path('myevents/', views.myevents, name="myevents"),
    path('create_event/', views.create_event, name="create_event"),
    path('create_activity/', views.create_activity, name="create_activity"),
    path('update_event/<int:id>', views.update_event, name="update_event"),
    path('update_activity/<int:id>', views.update_activity, name="update_activity"),
    path('delete_event/<int:id>', views.delete_event, name="delete_event"),
    path('delete_activity/<int:id>', views.delete_activity, name="delete_activity")
]
