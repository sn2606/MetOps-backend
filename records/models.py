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
    pressure = models.DecimalField(max_digits=10, decimal_places=4)
    relative_humidity = models.DecimalField(max_digits=10, decimal_places=4)
    wind_speed = models.DecimalField(max_digits=10, decimal_places=4)
    wind_direction = models.DecimalField(max_digits=10, decimal_places=4)

    @property
    def virtual_temp(self):
        """
        Return Virtual Temperature given Temperature, Pressure and Relative Humiditys
        """
        T = float(self.temperature)
        p = float(self.pressure)
        rh = float(self.relative_humidity)
        exp = 7.5*(T/(T + 237.7))
        es = 6.11 * pow(10, exp)
        ws = 621.9569100577033 * (es/(p - es))
        w = rh * ws
        vt = T * ((w + 0.6219569100577033)/(0.6219569100577033 * (1 + w)))
        return "%.4f" % vt


class RecordForQuery(models.Model):
    """
    Normalization of database: to get the record ids that correspond to a query and vice versa
    """
    id = models.BigAutoField(primary_key=True)
    query_id = models.ForeignKey(
        MetQuery, related_name='query_id', on_delete=models.CASCADE)
    record_id = models.OneToOneField(
        Record, related_name='record_id', on_delete=models.CASCADE)
