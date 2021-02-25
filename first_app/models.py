from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pocs', blank=True)

    def __str__(self):
        return self.user.username