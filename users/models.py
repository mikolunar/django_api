from django.db import models
from django.contrib.auth.models import User

from cvapp.models import CV


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete='models.CASCADE')
    cv = models.ManyToManyField(CV)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


# Create your models here.
