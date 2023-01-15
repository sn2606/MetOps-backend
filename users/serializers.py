from rest_framework import serializers
from django.contrib.auth.validators import UnicodeUsernameValidator

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_no',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        # username_regex = r"^[\w.@+-]+\Z"
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError(
                'Password and Confirm Password does not match.')

        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    username_validator = UnicodeUsernameValidator()

    username = serializers.CharField(
        max_length=150, validators=[username_validator])

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'full_name',
            'email',
            'phone_no',
        ]
