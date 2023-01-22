from rest_framework import serializers
from .models import Exercise, Journal, Workout, User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        user = User.objects.create(
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        email=validated_data['email'],
        username=validated_data['username'],
        password= make_password(validated_data['password'])
        )
        user.save()
        print(user)
        return user

    def update(self, instance, validated_data):
        user = User.objects.get(email=validated_data["email"])
        user.password = make_password(validated_data["password"])
        user.save()
        return user

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'