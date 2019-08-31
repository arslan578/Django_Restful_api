from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class CustomAuthenticateUsersManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email Field Is Required")

        if not username:
            raise ValueError("Username Field Is Required")

        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, staff_member, password=None):

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            staff_member=staff_member
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomAuthenticateUsers(AbstractBaseUser):

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    staff_member = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now=True, null=True)
    last_login = models.DateTimeField(auto_now=True, null=True)
    user_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomAuthenticateUsersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'staff_member']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, per):
        return True
