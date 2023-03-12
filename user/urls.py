from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from user.views import UsersListAPIView, UserDetailAPIView, change_password



user_patterns = [
    path('', UsersListAPIView.as_view()),
    path('<int:pk>', UserDetailAPIView.as_view()),
    path('change_password', change_password, name='change_password'),

]

token_patterns = [
    path('', TokenObtainPairView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
]

urlpatterns = [
    path('users/', include(user_patterns)),
    path('token/', include(token_patterns)),
]