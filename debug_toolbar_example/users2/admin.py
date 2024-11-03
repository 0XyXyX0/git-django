from django.contrib import admin

from users2.models import Citizen, Passport, Post, UserProfile

admin.site.register(Citizen)
admin.site.register(Passport)
admin.site.register(UserProfile)
admin.site.register(Post)