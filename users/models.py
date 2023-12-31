from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField
from organization.models import Organization
import random


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Users must have an email address"))
        if password is None:
            raise ValueError(_("Password is compulsory"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(PermissionsMixin, AbstractBaseUser):
    # by default django uses auto increament for the id
    # uncomment org_id when organization model has been created
    org_id = models.ForeignKey(Organization, verbose_name=_(
        "organisation name"), on_delete=models.CASCADE, null=True)
    first_name = models.CharField(_("first name"), max_length=225)
    last_name = models.CharField(
        _("last name"), max_length=225, blank=True, null=True)
    profile_pic = CloudinaryField(_("profile pic"))
    email = models.EmailField(_("email address"), max_length=225, unique=True)
    phone = models.CharField(
        _("phone number"), max_length=20, null=True, blank=True)
    refresh_token = models.TextField(_("refresh token"), blank=True, null=True)
    bank_number = models.CharField(
        _("bank number"), max_length=50, blank=True, null=True)
    bank_code = models.CharField(
        _("bank code"), max_length=50, blank=True, null=True)
    bank_name = models.CharField(
        _("bank name"), max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(_("created date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated date"), auto_now=True)
    lunch_credit_balance = models.CharField(_("lunch credit"), max_length=50)
    is_active = models.BooleanField(default=True)  # Add is_active field
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group', verbose_name='groups', blank=True, related_name='custom_users_groups')
    user_permissions = models.ManyToManyField(
        'auth.Permission', verbose_name='user permissions', blank=True, related_name='custom_users_permissions')

    @staticmethod
    def generate_reset_token(length):
        ret = (random.randint(0, 9).__str__() for _ in range(length))
        return ''.join(ret)
    password_reset_token = models.CharField(max_length=5, default=generate_reset_token(5), editable=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
