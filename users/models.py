from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(max_length=13, unique=True)
    invite_code = models.CharField(max_length=6, unique=True)
    invited_by = models.CharField(max_length=6, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number
