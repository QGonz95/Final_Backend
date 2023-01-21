from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Exercise, Journal, Workout, User

admin.site.register(User, UserAdmin)
admin.site.register(Exercise)
admin.site.register(Journal)
admin.site.register(Workout)
