from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, fullname, username, password, email, **extra_fields):
        user = self.model(fullname = fullname, username = username, password = password, email = email, **extra_fields)
        email = self.normalize_email(email)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, fullname, username, password, email, **extra_fields):
        return self._create_user(fullname, username, password, email, **extra_fields)

    def create_superuser(self, fullname, username, password, email, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(fullname, username, password, email, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length = 150)
    username = models.CharField(max_length = 100, unique = True)
    cellphone = models.CharField(max_length = 15)
    email = models.EmailField()
    is_staff = models.BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fullname, email']