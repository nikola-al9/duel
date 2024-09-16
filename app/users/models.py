import uuid
from attr import has

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager as BUM,
    PermissionsMixin,
    AbstractBaseUser,
    Group,
    Permission
)

from app.common.models import BaseModel, CompanyBaseModel
from django.utils.translation import gettext_lazy as _
from django.db.models.functions import Concat
from django.db.models import Value

# Taken from here:
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
# With some modifications


class BaseUserManager(BUM):
    def create_user(self, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email.lower()),
            is_active=is_active,
            is_admin=is_admin
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user

class Account(BaseModel, AbstractBaseUser):

    name = models.CharField(max_length=80, blank=True, null=True, default=None)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    last_login = models.DateTimeField(verbose_name="last_login", blank=True, null=True, default=None)
    points = models.IntegerField(default=100)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = BaseUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm: str):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table = 'account'


class RegistrationTokenEmail(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=80, blank=True, null=True, default=None)
    token = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    is_expired = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'registration_token_email'
