from django.urls import path

from .views import RegistrationView, LoginView

app_name = 'accounts'

urlpatterns = [
    path("signup/", RegistrationView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", RegistrationView.as_view(), name="profile"),
]
