from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    GENDER = (
        ('','Select your gender'),
        ('male','male'),
        ('famale','famale'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    full_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=16,choices=GENDER)
    birthdate =  models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="profile_images/")
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)



