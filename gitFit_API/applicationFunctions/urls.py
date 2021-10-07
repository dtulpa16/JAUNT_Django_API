from django.urls import path
from . import views

urlpatterns = [
    path('workout/', views.WorkoutList.as_view()),
    path('workout/<int:user_id>/', views.ViewClientWorkout.as_view()),
    path('assign/', views.AssignTrainer.as_view()),
    path('clients/<trainer_id>/', views.TrainerClients.as_view()),
    path('trainer/<client_id>/', views.ClientsTrainer.as_view()),
    path('forumpost/', views.ForumPostList.as_view()),
    path('forumreply/', views.ForumReplyList.as_view()),
    path('review/', views.TrainerReviews.as_view()),
    path('review/<int:user_id>/', views.TrainerReviewDetails.as_view()),
    path('trainerblog/', views.TrainerBlogList.as_view()),
    path('trainerblog/<int:user_id>/', views.TrainerBlogDetail.as_view()),
]