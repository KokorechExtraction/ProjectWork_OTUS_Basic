from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, UserModel
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Введите email"}),
    )
    phone_number = forms.CharField(

        required=False,
        label="Номер телефона",
        widget=forms.DateInput(attrs={"class": "form-control", "placeholder": "Введите номер телефона"})
    )
    class Meta:
        model = get_user_model()
        fields = ("email", 'phone_number', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        UserModel = get_user_model()
        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует")
        return email


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        required=True,
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Введите email"}),
    )

    def clean_username(self):

        username = self.cleaned_data.get("username")
        if not UserModel.objects.filter(email=username).exists():

            raise forms.ValidationError("Пользователя с таким email не существует")

        return username


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ("email", "username", "phone_number", "date_of_birth", "avatar", "first_name", "last_name")
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'phone_number': 'Номер телефона',
            'date_of_birth': 'Дата рождения',
            'avatar': 'Аватар',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

    def clean_username(self):

        username = self.cleaned_data.get("username")

        if len(username) <3:

            raise ValidationError('Имя пользователя быть более 5 символов')
        if UserModel.objects.filter(username=username).count() > 1:
            raise forms.ValidationError("Пользователь с таким username уже существует")
        return username


    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        UserModel = get_user_model()
        if UserModel.objects.filter(email=email).count() > 1:
            raise forms.ValidationError("Пользователь с таким email уже существует")
        return email

    def clean_phone_number(self):
        if self.cleaned_data.get("phone_number"):
            phone_number = self.cleaned_data.get("phone_number").lower()
            UserModel = get_user_model()

            if UserModel.objects.filter(phone_number=phone_number).count() > 1:
                raise forms.ValidationError("Пользователь с таким phone_number уже существует")
            if len(phone_number) < 3:
                raise forms.ValidationError("Телефонный номер должен включать 3 цифры")
            return phone_number