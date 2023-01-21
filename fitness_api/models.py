from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.CharField(max_length=255, blank=True, unique=True)
    passowrd =  models.CharField(max_length=255)
    username =  models.CharField(max_length=255, unique=True)

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    sets = models.IntegerField(blank=True)
    reps = models.IntegerField(blank=True)
    length = models.DurationField(blank=True)
    description = models.TextField(blank=True)


class Journal(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField(unique=True )
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='_entries')

class Workout_Logs(models.Model):
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    exercise = models.ManyToManyField(Exercise)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_logs')


