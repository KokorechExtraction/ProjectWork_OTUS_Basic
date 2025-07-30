from django.urls import path


from .views import RegisterView, CustomLoginView, CustomLoginOutView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLoginOutView.as_view(), name="logout"),
]