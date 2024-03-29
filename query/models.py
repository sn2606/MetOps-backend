from django.db import models
import requests

from users.models import User

# Create your models here.


class MetQuery(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    location = models.CharField(max_length=100, blank=True)


class QueryForUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, related_name='user_id', on_delete=models.CASCADE)
    query_id = models.OneToOneField(
        MetQuery, related_name='query_id_main', on_delete=models.CASCADE)
