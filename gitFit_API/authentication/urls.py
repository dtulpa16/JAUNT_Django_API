from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, UserDetail
from . import views

urlpatterns =[
    path('login/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('register/', views.RegisterView.as_view(), name = 'register'),
    path('<int:pk>/', views.UserDetail.as_view())
]