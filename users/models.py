from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):

    photo  = models.ImageField(upload_to='users/images/%Y/%m/%d',blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

    def __str__(self):
        return self.username
    