from rest_framework import serializers

from .models import MetQuery, QueryForUser


class MetQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = MetQuery
        fields = [
            'id',
            'created',
            'latitude',
            'longitude',
            'location'
        ]


class QueryForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryForUser
        fields = '__all__'
