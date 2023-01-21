from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.CharField(max_length=255, blank=True, unique=True)
    password =  models.CharField(max_length=255)
    username =  models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.username}"

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    sets = models.IntegerField(blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    length = models.DurationField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"

class Journal(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)
    
class Workout(models.Model):
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    exercise = models.ManyToManyField(Exercise)
    user = models.ForeignKey(User, related_name='logs', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

