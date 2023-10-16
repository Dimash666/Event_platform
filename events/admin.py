from django.contrib import admin
from events.models import Event, Comment, Attendance

admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(Attendance)
