from django.db import models
from apps.users.models import User


class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name