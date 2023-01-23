from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, unique=True)
    password =  models.CharField(max_length=255)
    username =  models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.username}"


class Journal(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)
    

class Goal(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField(blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    injuries = models.TextField(blank=True, null=True)
    progress_img = models.ImageField(upload_to='fitness_api/files/progress')
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='your_goal', on_delete=models.CASCADE)
    