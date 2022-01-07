from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class User(AbstractUser): 
    groups = models.ManyToManyField(Group, related_name='%(class)s_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='%(class)s_permissions')

    class Meta:
        ordering = ["-date_joined"]

class SubUser(AbstractUser):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='%(class)s_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='%(class)s_permissions')

    class Meta:
        ordering = ["-date_joined"]