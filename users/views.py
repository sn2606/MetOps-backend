from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import UserRegistrationSerializer, UserSerializer

# Create your views here.


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'message': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
