from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50, null=True)
    group = models.CharField(max_length=50, null=True)
    course = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=50, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    about = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=50, null=True)
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    spots = models.IntegerField(null=True)
    spots_taken = models.IntegerField(null=True)
    about = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class StudentToActivity(models.Model):
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    activity = models.ForeignKey(Activity, null=True, on_delete=models.SET_NULL)

