from django.urls import path
from . import views

urlpatterns = [
    path('api/user', views.UserList.as_view(), name='user_list'),
    path('api/user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api/journal', views.JournalList.as_view(), name='journal_list'),
    path('api/journal/<int:pk>', views.JournalDetail.as_view(), name='journal_detail'),
    path('api/exercise', views.ExerciseList.as_view(), name='exercise_list'),
    path('api/exercise/<int:pk>', views.ExerciseDetail.as_view(), name='exercise_detail'),
    path('api/workout', views.WorkoutList.as_view(), name='workout_list'),
    path('api/workout/<int:pk>', views.WorkoutDetail.as_view(), name='workout_detail'),
]