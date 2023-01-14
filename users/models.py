from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.formfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    phone_no = PhoneNumberField(region='IN')

    REQUIRED_FIELDS = [phone_no]
