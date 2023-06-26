from django.urls import path

from src.apps.users.views import UserAccountCreateAPIView, UserAccountLoginView, VerifyAccountAPIView


urlpatterns = [
    path('signup/', UserAccountCreateAPIView.as_view(), name='create-user-account'),
    path('login/', UserAccountLoginView.as_view(), name='login-user-account'),
    path('verify-account/<str:token>/', VerifyAccountAPIView.as_view(), name='verify-user-account'),
]
