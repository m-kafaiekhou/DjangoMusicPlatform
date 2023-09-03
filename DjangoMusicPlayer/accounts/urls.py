from django.urls import path

from .views import (
    RegistrationView,
    LoginView,
    LogoutView,
    PasswordResetConfirmView,
)

app_name = 'accounts'

urlpatterns = [
    path("signup/", RegistrationView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", RegistrationView.as_view(), name="profile"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm",),
]
