from .forms import RegistrationForm
from django.urls import reverse_lazy
from django.views import generic


class RegistrationView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
