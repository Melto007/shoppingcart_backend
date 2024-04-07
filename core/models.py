from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractUser
)
from django.core.exceptions import ValidationError
import datetime
import pytz

"""custom user model"""
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **fields):
        if not email:
            raise ValidationError("email is required")

        user = self.model(email=self.normalize_email(email), **fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValidationError("email is required")

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

CUSTOMER_CHOICE = (
    ("CUSTOMER", "CUSTOMER"),
    ("SHOP", "SHOP")
)

class User(AbstractUser):
    username = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, max_length=255, null=False, blank=False)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(unique=True, max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    choice = models.CharField(max_length=255, null=False, blank=False, choices=CUSTOMER_CHOICE)
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()