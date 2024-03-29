from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django.apps import apps
from django.utils.translation import gettext_lazy as _

# Create your models here.

#  Custom User Manager


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, phone_no, password=None, password2=None):
        """
        Creates and saves a User with the given username, first_name, last_name, email, phone_no and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError("The given username must be set")

        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            phone_no=phone_no,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_no, password=None):
        """
        Creates and saves a superuser with the given email, phone_no and password.
        """
        user = self.create_user(
            email,
            password=password,
            phone_no=phone_no,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#  Custom User Model


class User(AbstractBaseUser):
    """
    A user of the application
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    phone_no = PhoneNumberField(region="IN")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone_no']

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
