from django.db import models
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from user_app.models import CustomUser

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="user")
    bio = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.user



class Post(models.Model):
    author = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="post")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes_counter = models.IntegerField(default=0,)

    tags = models.ManyToManyField('Tag', related_name='posts')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.author


class Comment(models.Model):
    author = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.author}'s comment"


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name