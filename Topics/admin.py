from django.contrib import admin

from .models import Topic, Feed, New

admin.site.register(Topic)
admin.site.register(Feed)
admin.site.register(New)
