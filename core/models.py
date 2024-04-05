from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)
from django.core.exceptions import ValidationError

"""custom user model"""
class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **fields):

        if not username:
            raise ValidationError("username is required")

        if not email:
            raise ValidationError("email is required")

        user = self.model(username=username, email=self.normalize_email(email), **fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **fields):
        if not username:
            raise ValidationError("username is required")

        if not email:
            raise ValidationError("email is required")

        user = self.create_user(username=username, email=email, **fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    username = models.CharField(
        unique=True,
        max_length=255,
        null=False,
        blank=False
    )
    email = models.EmailField(
        unique=True,
        max_length=255,
        null=False,
        blank=False
    )
    company_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        unique=True,
        max_length=255,
        null=False,
        blank=False
    )
    password = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()