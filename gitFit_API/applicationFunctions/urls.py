from django.urls import path
from . import views

urlpatterns = [
    path('workout/', views.WorkoutList.as_view()),
    path('workout/<int:user_id>/', views.ViewClientWorkout.as_view()),
    path('assign/', views.AssignTrainer.as_view()),
    path('clients/<trainer_id>/', views.TrainerClients.as_view()),
    path('forumpost/', views.ForumPostList.as_view()),
    path('forumreply/', views.ForumReplyList.as_view()),
]