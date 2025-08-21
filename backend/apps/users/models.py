from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Make email the unique identifier
    email = models.EmailField(unique=True)

    # Keep username, but make it optional/for display
    username = models.CharField(max_length=150, unique=True)

    # Tell Django to use email for authentication
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # still ask for username when creating a user

    def __str__(self):
        return self.email
