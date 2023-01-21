from django.contrib import admin
from .models import Exercise, Journal, Workout, User

admin.site.register(User)
admin.site.register(Exercise)
admin.site.register(Journal)
admin.site.register(Workout)
