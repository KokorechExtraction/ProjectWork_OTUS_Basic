from django.urls import path

from .views import CreateProfilePageView, ProfileDetailView

urlpatterns = [
    path("profile_detail/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("create_profile/", CreateProfilePageView.as_view(), name="create_profile"),

]