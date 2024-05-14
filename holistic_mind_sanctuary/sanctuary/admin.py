from django.contrib import admin
from .models import Zone, Service, Event, Post

admin.site.register(Zone)
admin.site.register(Service)
admin.site.register(Event)
admin.site.register(Post)

