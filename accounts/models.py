from django.db import models
from django.contrib.auth.models import AbstractUser
from .user_manager import CustomUserManager
# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=120)


    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email