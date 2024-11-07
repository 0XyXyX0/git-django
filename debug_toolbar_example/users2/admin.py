from django.contrib import admin

from users2.models import Citizen, Passport, Post, UserProfile, Event

admin.site.register(Citizen)
admin.site.register(Passport)
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Event)