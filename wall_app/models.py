from django.db import models
from user_app.models import CustomUser

class Post(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="post")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes_counter = models.IntegerField(default=0,)

    tags = models.ManyToManyField('Tag', related_name='posts')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.author

class Comment(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.author}'s comment"



class AuthorProfile(models.Model):
    author = models.OneToOneField("CustomUser", on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()

    def __str__(self):
        return self.author

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name