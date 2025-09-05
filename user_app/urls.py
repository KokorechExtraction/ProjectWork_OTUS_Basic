from django.urls import path
# from django.contrib.auth import views as auth_views
from .views import RegisterView, CustomLoginView, CustomLoginOutView, CustomProfileView, IndexTemplateView, CustomProfileChangeView, CustomPasswordChangeView

urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLoginOutView.as_view(), name="logout"),
    path("profile/<int:pk>/", CustomProfileView.as_view(), name="profile"),
    path("profile/<int:pk>/edit/", CustomProfileChangeView.as_view(), name="edit_profile"),
    path('profile/<int:pk>/password/', CustomPasswordChangeView.as_view(), name="password"),
]