from django.urls import path

from .views import GetVerificationCodeView, LoginView, UsersListView, UserProfileView

urlpatterns = [
    path('auth/get_code/', GetVerificationCodeView.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('users/', UsersListView.as_view()),
    path('profile/', UserProfileView.as_view())
]
