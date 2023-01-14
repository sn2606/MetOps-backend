from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

# Create your models here.


class UserPhoneNo(models.Model):
    """
    Phone No. of a User
    """
    user_phone_id = models.OneToOneField(
        User, related_name='phone_of_user_id', on_delete=models.CASCADE)
    phone_no = PhoneNumberField(region='IN')
