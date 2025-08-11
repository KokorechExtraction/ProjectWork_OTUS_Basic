from django.urls import path

from .views import RegisterView, CustomLoginView, CustomLoginOutView, CustomProfileView, IndexTemplateView

urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLoginOutView.as_view(), name="logout"),
    path("profile/", CustomProfileView.as_view(), name="profile"),
]