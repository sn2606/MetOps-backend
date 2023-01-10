from django.db import models
from query.models import MetQuery
from metpy.calc import virtual_temperature, mixing_ratio_from_relative_humidity
from metpy.units import units

# Create your models here.


class Record(models.Model):
    id = models.BigAutoField(primary_key=True)
    height = models.IntegerField()
    temperature = models.DecimalField(max_digits=10, decimal_places=4)
    pressure = models.DecimalField(max_digits=10, decimal_places=4)
    relative_humidity = models.DecimalField(max_digits=10, decimal_places=4)
    wind_speed = models.DecimalField(max_digits=10, decimal_places=4)
    wind_direction = models.DecimalField(max_digits=10, decimal_places=4)

    @property
    def virtual_temp(self):
        p = self.pressure * units.hPa
        T = self.temperature * units.degC
        rh = self.relative_humidity / 100
        mix_ratio = mixing_ratio_from_relative_humidity(p, T, rh).to('g/kg')
        return virtual_temperature(T, mix_ratio * units('g/kg'))


class RecordForQuery(models.Model):
    id = models.BigAutoField(primary_key=True)
    query_id = models.ForeignKey(
        MetQuery, related_name='query_id', on_delete=models.CASCADE)
    record_id = models.ForeignKey(
        Record, related_name='record_id', on_delete=models.CASCADE)
