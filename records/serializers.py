from rest_framework import serializers

from .models import Record, RecordForQuery


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = [
            'id',
            'height',
            'temperature',
            'pressure',
            'relative_humidity',
            'wind_speed',
            'wind_direction',
            'virtual_temp'
        ]


class RecordForQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordForQuery
        fields = '__all__'
