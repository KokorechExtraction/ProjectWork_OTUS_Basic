from django.urls import path


from .views import ProfileDetailView, UserPostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, \
    ProfileListView

urlpatterns = [
    path("profiles/", ProfileListView.as_view(), name="profiles"),
    path("profile_detail/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("wall/<int:pk>/", UserPostListView.as_view(), name="wall"),
    path("post_create/<int:pk>/", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/edit/<int:pk>/", PostUpdateView.as_view(), name="post_edit"),
    path("posts/delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
]