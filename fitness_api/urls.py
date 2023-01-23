from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('api/user', views.UserList.as_view(), name='user_list'),
    path('api/user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api/journal', views.JournalList.as_view(), name='journal_list'),
    path('api/journal/<int:pk>', views.JournalDetail.as_view(), name='journal_detail'),
    path('api/goal', views.GoalList.as_view(), name='goal_list'),
    path('api/goal/<int:pk>', views.GoalDetail.as_view(), name='goal_detail'),
    path('api/useraccount/login', csrf_exempt(views.check_login), name="check_login")
]

