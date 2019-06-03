from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, info, password1, password2):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            info=info,
        )
        user.set_password(password1)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    idx = models.AutoField(primary_key=True)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=32)
    info = models.TextField(default="Write to Information")
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser


class Apikey(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    api_key = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
