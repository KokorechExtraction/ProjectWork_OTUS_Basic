from django.urls import path


from .views import ProfileDetailView, UserPostListView, PostCreateView, PostDetailView

urlpatterns = [
    path("profile_detail/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("wall/<int:pk>/", UserPostListView.as_view(), name="wall"),
    path("post_create/<int:pk>/", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]