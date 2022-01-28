from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field import modelfields
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **kwargs):
        print(kwargs)
        if not email:
            raise ValueError(_("Provide email!"))
        email = self.normalize_email(email)
        user = self.model(
            email=email, user_name=user_name, first_name=first_name, **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, first_name, password, **kwargs):
        kwargs.setdefault("is_admin", True)
        kwargs.setdefault("is_superuser", True)
        return self.create_user(email, user_name, first_name, password, **kwargs)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(_("email addres"), unique=True)
    user_name = models.CharField(max_length=250, unique=True)
    phone = modelfields.PhoneNumberField(
        _("phone number"), unique=True, blank=True, null=True
    )
    birthday = models.DateField(null=True, blank=True)
    city = models.ForeignKey(
        "City",
        verbose_name=_("City"),
        related_name="user",
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    about = models.TextField(_("about"), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name", "first_name"]

    def __str__(self):
        return self.user_name


class City(models.Model):
    name = models.CharField(_("City"), max_length=200)

    def __str__(self):
        return self.name
