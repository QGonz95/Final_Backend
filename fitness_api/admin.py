from django.contrib import admin
from .models import Journal, Goal, User

admin.site.register(User)
admin.site.register(Journal)
admin.site.register(Goal)
