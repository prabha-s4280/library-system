from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_Number=models.CharField(max_length=10)
    Address=models.CharField(max_length=50)
    College_name=models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
