from .forms import RegistrationForm, LoginForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic, View
from django.contrib.auth.views import auth_login, auth_logout, PasswordResetConfirmView
from django.contrib import messages
from django.contrib.auth import authenticate


class RegistrationView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("accounts:profile")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return redirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(self.request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user:
            remember = self.request.POST.get('remember')
            if not remember:
                self.request.session.set_expiry(0)
            auth_login(self.request, user)
            return redirect(self.get_success_url())
        else:
            messages.info(self.request, "Invalid username or password", "info")
            return redirect(reverse_lazy('accounts:login'))


class LogoutView(View):
    success_url = reverse_lazy('accounts:login')

    def post(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect(self.success_url)


class PasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:login')
