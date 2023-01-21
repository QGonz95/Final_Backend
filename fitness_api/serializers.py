from rest_framework import serializers
from .models import Exercise, Journal, Workout_Logs, User

class UserSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'passowrd', 'username')

class ExerciseSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'sets', 'reps', 'length', 'description')

class JournalSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'title', 'body', 'created_on')

class Workout_LogsSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Workout_Logs
        fields = ('id', 'title', 'created_on')
    
class Workout_LogsSerializer(Workout_LogsSerializerBase):
    user = UserSerializerBase()
    exercise = ExerciseSerializerBase(many=True)
    class Meta(Workout_LogsSerializerBase.Meta):
        fields = Workout_LogsSerializerBase.Meta.fields + ('exercise', 'user')

class JournalSerializer(JournalSerializerBase):
    user = UserSerializerBase()
    class Meta(JournalSerializerBase.Meta):
        fields = JournalSerializerBase.Meta.fields + ('user',)
    
class ExerciseSerializer(ExerciseSerializerBase):
    logs_set = Workout_LogsSerializerBase(many=True)
    user = UserSerializerBase()
    class Meta(ExerciseSerializerBase.Meta):
        fields = ExerciseSerializerBase.Meta.fields + ('logs_set', 'user')

class UserSerializer(UserSerializerBase):
    _exercise = ExerciseSerializerBase(many=True)
    _entries = JournalSerializerBase(many=True)
    _logs = Workout_LogsSerializerBase(many=True)
    class Meta(UserSerializerBase.Meta):
        fields = UserSerializerBase.Meta.fields + ('_exercise', '_entries', '_logs')