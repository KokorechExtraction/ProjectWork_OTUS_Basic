from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView, DetailView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm
from .task import send_info_email
from django.contrib.auth import login
from django.contrib import messages

from .models import CustomUser


class IndexTemplateView(TemplateView):
    template_name = "index.html"


class RegisterView(FormView):
    template_name = "user_app/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        send_info_email.delay(
            recipient_email='user@example.com',
            subject='Аккаунт успешно зарегистрирован',
            message='Аккаунт успешно зарегистрирован'
        )
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = "user_app/login.html"
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("index")

    def get_success_url(self):
        return self.success_url


class CustomLoginOutView(LogoutView):
    next_page = reverse_lazy("login")


class CustomProfileView(DetailView):
    model = CustomUser
    template_name = "user_app/profile.html"
    context_object_name = "profile"

class CustomProfileChangeView(UpdateView):
    model = CustomUser
    template_name = "user_app/edit_profile.html"
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        messages.success(self.request, 'Профиль успешно обновлен')
        return super().form_valid(form)