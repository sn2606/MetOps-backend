from rest_framework import serializers

from .models import Record, RecordForQuery


class MetQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class RecordForQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordForQuery
        fields = '__all__'
