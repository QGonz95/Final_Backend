from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import UserSerializer, ExerciseSerializer, JournalSerializer, WorkoutSerializer
from .models import User, Exercise, Journal, Workout


# Create your views here.
class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class ExerciseList(generics.ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Exercise.objects.all().order_by('id')
    serializer_class = ExerciseSerializer

class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all().order_by('id')
    serializer_class = ExerciseSerializer

class JournalList(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Journal.objects.all().order_by('id')
    serializer_class = JournalSerializer

class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    search_fields = ['title']
    queryset = Journal.objects.all().order_by('id')
    serializer_class = JournalSerializer

class WorkoutList(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = Workout.objects.all().order_by('id')
    serializer_class = WorkoutSerializer

class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all().order_by('id')
    serializer_class = WorkoutSerializer

