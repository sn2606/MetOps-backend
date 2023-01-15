from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegistrationSerializer, UserLoginSerializer, AccountSerializer

# Create your views here.


def get_tokens_for_user(user):
    """
    Generate Token Manually
    """
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    """
    Class based view to register the user
    """

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token': token, 'message': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    """
    Class based view to login the user
    """

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'message': 'Login Successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'errors': {'non_field_errors': ['Meow']}}, status=status.HTTP_404_NOT_FOUND)


class AccountView(APIView):
    """
    Get account information of logged in user
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = AccountSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
