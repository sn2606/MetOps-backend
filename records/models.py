from django.db import models
from query.models import MetQuery

# Create your models here.


class Record(models.Model):
    """
    Values of one row in the data table
    """
    id = models.BigAutoField(primary_key=True)
    height = models.IntegerField()
    temperature = models.DecimalField(max_digits=10, decimal_places=4)
    virtual_temperature = models.DecimalField(max_digits=10, decimal_places=4)
    pressure = models.DecimalField(max_digits=10, decimal_places=4)
    relative_humidity = models.DecimalField(max_digits=10, decimal_places=4)
    wind_speed = models.DecimalField(max_digits=10, decimal_places=4)
    wind_direction = models.DecimalField(max_digits=10, decimal_places=4)


class RecordForQuery(models.Model):
    """
    Normalization of database: to get the record ids that correspond to a query and vice versa
    """
    id = models.BigAutoField(primary_key=True)
    query_id = models.ForeignKey(
        MetQuery, related_name='query_id', on_delete=models.CASCADE)
    record_id = models.OneToOneField(
        Record, related_name='record_id', on_delete=models.CASCADE)
