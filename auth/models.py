from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):   

    class Meta:
        ordering = ["-date_joined"]

class SubUser(AbstractUser):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date_joined"]