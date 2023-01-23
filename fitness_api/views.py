from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import UserSerializer, GoalSerializer, JournalSerializer
from .models import User, Journal, Goal
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json

# Create your views here.
class JournalList(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Journal.objects.all().order_by('id')
    serializer_class = JournalSerializer

class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    search_fields = ['title']
    queryset = Journal.objects.all().order_by('id')
    serializer_class = JournalSerializer

class GoalList(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = Goal.objects.all().order_by('id')
    serializer_class = GoalSerializer

class GoalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all().order_by('id')
    serializer_class = GoalSerializer

class ProfileGoalList(generics.ListAPIView):
    serializer_class = GoalSerializer
    
    def get_queryset(self):
        queryset = Goal.objects.all().order_by('id')
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user_id = user)
        return queryset

class ProfileEntryList(generics.ListAPIView):
    serializer_class = JournalSerializer

    def get_queryset(self):
        queryset = Journal.objects.all().order_by('id')
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user_id = user)
        return queryset


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')

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
                return JsonResponse({'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'username':user.username, 'email': user.email})
            else:
                return JsonResponse({'password' : 'Incorrect password'}, status=500)
        except:
            return JsonResponse({'email' : 'Email does not exist'}, status=500)