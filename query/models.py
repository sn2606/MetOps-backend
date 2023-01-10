from django.db import models
from django.contrib.auth import get_user_model
import requests

# Create your models here.
User = get_user_model()


class MetQuery(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)

    @property
    def location(self):
        url = f'http://api.positionstack.com/v1/reverse?access_key=00931655337dfe90ed40968a26def65a&query={self.latitude},{self.longitude}&limit=2&output=json'
        res = requests.get(url).json()
        if res['data']:
            location = f"{res['data'][0]['county']}, {res['data'][0]['region']}"
            return location
        else:
            return ''


class QueryForUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, related_name='user_id', on_delete=models.CASCADE)
    query_id = models.ForeignKey(
        MetQuery, related_name='query_id_main', on_delete=models.CASCADE)
