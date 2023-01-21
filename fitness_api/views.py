from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, ExerciseSerializer, JournalSerializer, Workout_LogsSerializer
from .models import User, Exercise, Journal, Workout_Logs
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json

# Create your views here.
class ExerciseList(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class JournalList(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class Workout_LogsList(generics.ListCreateAPIView):
    queryset = Workout_Logs.objects.all()
    serializer_class = Workout_LogsSerializer

class Workout_LogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout_Logs.objects.all()
    serializer_class = Workout_LogsSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

def check_login(request):
    if request.method=='Get':
        return JsonResponse({})

    if request.method=='PUT':
        JsonRequest = json.loads(request.body)
        email = JsonRequest['email']
        password = JsonRequest['password']
        try :
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return JsonResponse({'id': user.id, 'firstname': user.firstname, 'lastname': user.lastname, 'username':user.username, 'email': user.email})
            else:
                return JsonResponse({'password' : 'Incorrect password'}, status=500)
        except:
            return JsonResponse({'email' : 'Email does not exist'}, status=500)