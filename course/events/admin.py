from django.contrib import admin

from .models import *

admin.site.register(Student)
admin.site.register(Event)
admin.site.register(Activity)
admin.site.register(StudentToActivity)
