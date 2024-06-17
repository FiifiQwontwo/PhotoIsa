from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import MyUserManager
from django.core.exceptions import ValidationError


# Create your models here.

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(blank=True, upload_to='avatar/% Y/%m/%d',
                               validators=[
                                   FileExtensionValidator(
                                       allowed_extensions=['jpeg ', 'png', 'jpg', 'webm'])]
                               )
    username = models.CharField(max_length=20, unique=True)
    # required Fields
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def clean(self):
        if self.avatar:
            # Check the image width and height here if needed
            max_size = 1 * 1024 * 1024 * 1024
            if self.avatar.size > max_size:
                raise ValidationError("Image file too large ( > 1GB )")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name', 'username']

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, add_label):
        return True


class UserAgentInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_agent = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.user_agent}"