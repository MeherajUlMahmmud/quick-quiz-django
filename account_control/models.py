from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

from common.models import BaseModel


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, is_student=True, is_teacher=False, is_admin=False):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )

        user.set_password(password)

        user.is_student = is_student
        user.is_teacher = is_teacher
        user.is_admin = is_admin

        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_student = False
        user.is_teacher = False
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, BaseModel, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    password_plain = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = MyUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def get_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class UserOTPModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_otp')
    otp_code = models.CharField(max_length=255)
    otp_code_expired = models.DateTimeField()

    class Meta:
        verbose_name = 'User OTP'
        verbose_name_plural = 'User OTPs'

    def __str__(self):
        return self.user.username


class TeacherModel(BaseModel):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='teacher')
    total_courses = models.IntegerField(default=0)
    total_students = models.IntegerField(default=0)
    total_reviews = models.IntegerField(default=0)
    rating = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.user.username


class StudentModel(BaseModel):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='student')
    total_courses = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.user.username
