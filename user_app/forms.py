from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, UserModel
from django.contrib.auth import get_user_model




class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Введите email"}),
    )
    class Meta:
        model = get_user_model()
        fields = ("email",)

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        UserModel = get_user_model()
        if UserModel.objects.filter(email=email).exists():
            return forms.ValidationError("Пользователь с таким email уже существует")
        return email


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        required=True,
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Введите email"}),
    )

    def clean_username(self):
        username = self.cleaned_data.get("username").lower()
        if not UserModel.objects.filter(username=username).exists():
            return forms.ValidationError("Пользователя с таким email не существует")
        return username