from django.urls import path

from .views import ProfileView


urlpatterns = [
    path("profile_detail/<int:pk>/", ProfileView.as_view(), name="profile_detail"),

]