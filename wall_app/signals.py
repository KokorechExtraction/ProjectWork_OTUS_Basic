from django.db.models.signals import post_save
from user_app.models import CustomUser
from django.dispatch import receiver
from .models import AuthorProfile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        AuthorProfile.objects.create(author=instance)


# @receiver(post_save, sender=CustomUser)
# def save_profile(sender, instance, **kwargs):
#     instance.author.save()